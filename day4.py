import click
import collections

from datetime import datetime


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = f.read()

    text = text.split("\n")
    text.pop()

    data = {}

    for row in text:
        date_fragment, guard_information = row.split("] ")
        date_fragment = date_fragment[1:]

        date = datetime.strptime(date_fragment, "%Y-%m-%d %H:%M")
        data[date] = guard_information

    data = collections.OrderedDict(sorted(data.items()))

    if part == 1:
        part_one(data)
    else:
        part_two


def part_one(data):
    guards = {}
    guard_id = ""
    time = []
    duration = 0
    begin_minute = -1
    start = 0

    for date_time, guard_information in data.items():
        if start == 0:
            guard_id = guard_information.split(" ")[1][1:]
            start += 1
        elif "begins shift" in guard_information:
            if guard_id not in guards:
                guards[guard_id] = []

            guards[guard_id].append((time, duration))

            guard_id = guard_information.split(" ")[1][1:]
            time = []
            duration = 0
        elif guard_information == "falls asleep":
            begin_minute = date_time.minute
        else:
            time = time + [i for i in range(begin_minute, date_time.minute)]
            duration += date_time.minute - begin_minute

    max_guard = ("", 0)

    for guard_id, guard_information in guards.items():
        duration = sum([duration for time, duration in guard_information])

        if duration > max_guard[1]:
            max_guard = (guard_id, duration)

    minutes_asleep = []

    for list_asleep in guards[max_guard[0]]:
        minutes_asleep += list_asleep[0]

    count = collections.Counter(minutes_asleep)
    best_minute = count.most_common()[0][0]

    print(f"Guard ID: {max_guard[0]} - Best Minute: {best_minute}")
    print(
        f"Solution: {int(max_guard[0])} * {best_minute} = {int(max_guard[0]) * best_minute}"
    )


def part_two():
    pass


if __name__ == "__main__":
    main()
