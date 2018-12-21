import click


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = [int(number.strip()) for number in f.read().split()]

    if part == 1:
        print(part_one(text, 0)[0])
    else:
        print(part_two(text, 0)[0])


def part_one(text: list, start: int):
    meta_sum = 0
    num_nodes, num_meta = text[start : start + 2]
    next_start = start + 2

    for child_node in range(num_nodes):
        t_sum, next_start = part_one(text, next_start)
        meta_sum += t_sum
    meta_sum += sum(text[next_start : next_start + num_meta])

    return meta_sum, next_start + num_meta


def part_two(text: list, start: int):
    node_sum = 0
    num_nodes, num_meta = text[start : start + 2]
    next_start = start + 2

    if num_nodes:
        node_vals = []
        for child_node in range(num_nodes):
            t_sum, next_start = part_two(text, next_start)
            node_vals.append(t_sum)
        for idx in text[next_start : next_start + num_meta]:
            if idx - 1 < len(node_vals):
                node_sum += node_vals[idx - 1]
    else:
        node_sum += sum(text[next_start : next_start + num_meta])

    return node_sum, next_start + num_meta


if __name__ == "__main__":
    main()
