import click
import collections
import operator


@click.command()
@click.option("--part", default=2, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        instructions = [line.strip() for line in f.readlines()]

    dependencies = {}
    used_letters = set()

    for instruction in instructions:
        instruction = instruction.split()
        dependency = instruction[1]
        letter = instruction[7]

        if letter not in dependencies:
            dependencies[letter] = []

        dependencies[letter].append(dependency)
        used_letters.add(dependency)

    for letter in used_letters:
        if letter not in dependencies:
            dependencies[letter] = []

    dependencies = collections.OrderedDict(sorted(dependencies.items()))

    if part == 1:
        part_one(dependencies)
    else:
        part_two(dependencies)


def part_one(dependencies):
    order = []

    while len(dependencies):
        next = min(dependencies.items(), key=operator.itemgetter(1))[0]
        order.append(next)
        dependencies.pop(next)

        for key in dependencies.keys():
            if next in dependencies[key]:
                dependencies[key].remove(next)

    order = "".join(order)

    print(f"Correct order: {order}")


def part_two(dependencies):
    safe = {n: False for n in dependencies}
    todo = set(dependencies)
    done = set()

    update_safe(safe, dependencies)

    workers = 5
    time = 0
    in_progress = {}

    while todo:
        while workers > 0:
            safe_n = {n for n in safe if safe[n]}.intersection(todo)

            if not len(safe_n):
                break

            workers -= 1
            n = sorted(safe_n)[0]
            todo.remove(n)
            in_progress[n] = 60 + ord(n) - ord("A") + 1

        step = min(in_progress.values())
        time += step

        for n in list(in_progress):
            in_progress[n] -= step
            if in_progress[n] == 0:
                in_progress.pop(n)
                workers += 1
                dependencies = update_dependencies(n, dependencies)
                update_safe(safe, dependencies)
                done.add(n)

    print(f"Time needed: {time}")


def update_safe(safe, dependencies):
    for n in safe:
        if n in dependencies:
            if not len(dependencies[n]):
                safe[n] = True


def update_dependencies(n, dependencies):
    dependencies.pop(n)
    for key in dependencies.keys():
        if n in dependencies[key]:
            dependencies[key].remove(n)

    return dependencies


if __name__ == "__main__":
    main()
