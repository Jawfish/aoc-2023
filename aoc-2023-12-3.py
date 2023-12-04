from itertools import groupby
from math import prod


def is_in_range(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def get_adjacent_coords(x, y, grid):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return [(x + dx, y + dy) for dx, dy in dirs if is_in_range(x + dx, y + dy, grid)]


def get_part_numbers(schematic):
    part_numbers = {}

    for r, row in enumerate(schematic):
        groups = groupby(enumerate(row), lambda x: x[1].isdigit())

        for is_digit, group in groups:
            if is_digit:
                digits = list(group)
                num = "".join([char for _, char in digits])
                for c, _ in digits:
                    part_numbers[(r, c)] = int(num)

    return part_numbers


def sum_part_numbers(schematic):
    part_numbers = get_part_numbers(schematic)
    total_sum = 0

    def is_symbol(char):
        return not (char.isdigit() or char == ".")

    for (r, c), num in part_numbers.items():
        for adj_x, adj_y in get_adjacent_coords(r, c, schematic):
            if is_symbol(schematic[adj_x][adj_y]):
                total_sum += num
                break

    return total_sum


def sum_gear_ratios(schematic):
    part_numbers = get_part_numbers(schematic)
    sum = 0

    part_sets = [
        {
            part_numbers[coord]
            for coord in get_adjacent_coords(r, c, schematic)
            if coord in part_numbers
        }
        for r, row in enumerate(schematic)
        for c, cell in enumerate(row)
        if cell == "*"
    ]

    for p in part_sets:
        if len(p) == 2:
            sum += prod(p)

    return sum


def main():
    with open("input") as f:
        schematic = [line.strip() for line in f.readlines()]

    print(sum_part_numbers(schematic))
    print(sum_gear_ratios(schematic))


if __name__ == "__main__":
    main()
