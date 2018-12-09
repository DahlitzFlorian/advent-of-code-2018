"""Simple solution for day one"""
import click


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = f.read()

    lst = text.split("\n")
    lst.pop()  # Last element is always the empty string

    if part == 1:
        part_one(lst)
    else:
        part_two(lst)


def part_one(list_of_numbers: list):
    result = 0
    for element in list_of_numbers:
        result += int(element)

    print(result)


def part_two(list_of_number: list):
    result = 0
    used = []
    flag = True

    while flag:
        for element in list_of_number:
            result += int(element)
            if result in used:
                print(result)
                flag = False
                break

            used.append(result)


if __name__ == "__main__":
    main()
