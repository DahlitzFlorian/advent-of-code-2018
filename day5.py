import click


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = f.read()
        text = text.strip()

    if part == 1:
        part_one(text)
    else:
        part_two(text)


def part_one(text):
    polymer = list(text)

    stack = []
    for char in polymer:
        if not stack:
            stack.append(char)
        elif stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)

    print(f"Units remaining: {len(stack)}")


def part_two(text):
    shortest_polymer = ("", float("inf"))

    for letter in set(text.lower()):
        cleaned_text = [unit for unit in list(text) if unit.lower() != letter]
        stack = []

        for char in cleaned_text:
            if not stack:
                stack.append(char)
            elif stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)

        if len(stack) < shortest_polymer[1]:
            shortest_polymer = (letter, len(stack))

    print(f"Shortest Polymer: {shortest_polymer[0]}: {shortest_polymer[1]}")


if __name__ == "__main__":
    main()
