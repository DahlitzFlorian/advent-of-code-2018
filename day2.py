import click


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = f.read()

    lst = text.split("\n")
    lst.pop()  # last element is always the empty string

    if part == 1:
        part_one(lst)
    else:
        part_two(lst)


def part_one(ids: list):
    letter_occurs_twice = 0
    letter_occurs_three_times = 0

    for element in ids:
        unique_chars = set(element)
        two_found = False
        three_found = False

        for char in unique_chars:
            if element.count(char) == 2 and not two_found:
                letter_occurs_twice += 1
                two_found = True
            elif element.count(char) == 3 and not three_found:
                letter_occurs_three_times += 1
                three_found = True

    checksum = letter_occurs_three_times * letter_occurs_twice

    print(f"Twice: {letter_occurs_twice}")
    print(f"Three Times: {letter_occurs_three_times}")
    print(
        f"{letter_occurs_twice} * {letter_occurs_three_times} = {checksum} = your checksum"
    )


def part_two(ids: list):
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            different_chars = 0
            index = -1
            for l, (a, b) in enumerate(zip(ids[i], ids[j])):
                if a != b:
                    different_chars += 1
                    index = l

            if different_chars == 1:
                solution_list = list(ids[i])
                del solution_list[index]
                solution = "".join(solution_list)
                print(f"Solution: {solution}")


if __name__ == "__main__":
    main()
