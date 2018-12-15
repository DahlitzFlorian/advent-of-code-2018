import click
import itertools
import numpy as np

from collections import defaultdict


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        COORDINATES = [line.strip() for line in f.readlines()]

    DIM = 360
    board = np.zeros((DIM, DIM), dtype=np.uint8)

    if part == 1:
        part_one(board, DIM, COORDINATES)
    else:
        part_two(DIM, COORDINATES)


def part_one(board, DIM, COORDINATES):
    counts = defaultdict(int)

    for x, y in itertools.product(range(DIM), repeat=2):
        min_dist = float("inf")
        min_cells = []
        for c_idx, coordinate in enumerate(COORDINATES):
            c_y, c_x = (int(x) for x in coordinate.split(", "))
            dist = abs(x - c_x) + abs(y - c_y)
            if dist < min_dist:
                min_dist = dist
                min_cells = [c_idx]
            elif dist == min_dist:
                min_cells.append(c_idx)
        if len(min_cells) == 1:
            counts[min_cells[0]] += 1
            board[x][y] = min_cells[0]
        else:
            board[x][y] = "-1"

    border_cells = set()
    for i in range(DIM):
        border_cells.add(board[0][i])
        border_cells.add(board[DIM - 1][i])
        border_cells.add(board[i][0])
        border_cells.add(board[i][DIM - 1])

    max_val = 0
    for idx, val in counts.items():
        if idx in border_cells:
            continue
        if val > max_val:
            max_val = val

    print(f" Largest area that is not infinite: {max_val}")


def part_two(DIM, COORDINATES):
    safe = 0
    for x, y in itertools.product(range(DIM), repeat=2):
        total_dist = 0
        for c_idx, coordinate in enumerate(COORDINATES):
            c_y, c_x = (int(x) for x in coordinate.split(", "))
            dist = abs(x - c_x) + abs(y - c_y)
            total_dist += dist
        if total_dist < 10000:
            safe += 1

    print(f"Size of the region: {safe}")


if __name__ == "__main__":
    main()
