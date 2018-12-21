import click


@click.command()
@click.option(
    "--part",
    default=1,
    help="Part of the challenge (either 1 or 2)"
)
def main(part: int):
    with open("input") as f:
        text = f.read()

    text = text.split()
    players = int(text[0])
    last_marble = int(text[6])

    circle = [0]
    scores = [0] * players

    current_marble_position = 0

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[marble % players] += marble
            rem_idx = current_marble_position - 7
            rem_val = circle[rem_idx]
            current_marble_position = circle.index(circle[rem_idx])
            scores[marble % players] += rem_val
            circle.remove(rem_val)

        else:
            next_idx = current_marble_position + 2
            if next_idx == len(circle):
                circle.append(marble)
                current_marble_position = next_idx

            elif next_idx > len(circle):
                circle.insert(1, marble)
                current_marble_position = 1
            else:
                circle.insert(next_idx, marble)
                current_marble_position = next_idx

    print(f"The winning Elf's score is: {max(scores)}")


if __name__ == "__main__":
    main()
