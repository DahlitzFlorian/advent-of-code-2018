import click

from collections import namedtuple

Claim = namedtuple("Claim", "claim_id left_edge top_edge width height")


@click.command()
@click.option("--part", default=1, help="Part of the challenge (either 1 or 2)")
def main(part: int):
    with open("input") as f:
        text = f.read()

    text_claims = text.split("\n")
    text_claims.pop()

    claims = []

    for claim in text_claims:
        claim = claim.split()
        claim_id = claim[0][1:]
        left_edge, top_edge = claim[2][:-1].split(",")
        width, height = claim[3].split("x")

        claims.append(
            Claim(claim_id, int(left_edge), int(top_edge), int(width), int(height))
        )

    fabric_size = 1000

    fabric = [["." for _ in range(fabric_size)] for _ in range(fabric_size)]
    overlapping_claims = set()

    for position, claim in enumerate(claims):
        for vertical in range(claim.top_edge, claim.top_edge + claim.height):
            for horizontal in range(claim.left_edge, claim.left_edge + claim.width):
                if fabric[vertical][horizontal] == ".":
                    fabric[vertical][horizontal] = claim.claim_id
                else:
                    fabric[vertical][horizontal] += "," + claim.claim_id
                    for x in fabric[vertical][horizontal].split(","):
                        overlapping_claims.add(x)

    if part == 1:
        part_one(fabric, fabric_size)
    else:
        part_two(claims, overlapping_claims)


def part_one(fabric, fabric_size):
    count = 0
    for i in range(fabric_size):
        for j in range(fabric_size):
            if len(fabric[i][j].split(",")) > 1:
                count += 1

    print(f"Answer: {count}")


def part_two(claims, overlapping_claims):
    for claim in claims:
        if claim.claim_id not in overlapping_claims:
            print(f"ID: {claim.claim_id}")
            break


if __name__ == "__main__":
    main()
