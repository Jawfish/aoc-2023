from math import prod


def is_symbol(char):
    return not (char.isdigit() or char == ".")


def is_in_range(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])


def get_adjacent_coords(x, y, grid):
    adjacent = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dx, dy in dirs:
        if is_in_range(x + dx, y + dy, grid):
            adjacent.append((x + dx, y + dy))

    return adjacent


def sum_part_numbers(schematic):
    islands = []

    for r, row in enumerate(schematic):
        num = ""
        start_c = 0
        for c, cell in enumerate(row):
            if cell.isdigit():
                if num == "":
                    start_c = c
                num += cell
            elif num:
                islands.append((int(num), [(r, c_i) for c_i in range(start_c, c)]))
                num = ""

        if num:
            islands.append((int(num), [(r, c_i) for c_i in range(start_c, len(row))]))

    total_sum = 0

    for num, coords in islands:
        for r, c in coords:
            for adj_x, adj_y in get_adjacent_coords(r, c, schematic):
                if is_symbol(schematic[adj_x][adj_y]):
                    total_sum += num
                    break
            else:
                continue
            break

    return total_sum


def sum_gear_ratios(schematic):
    total_ratio_sum = 0
    part_numbers = {}

    for r, row in enumerate(schematic):
        c = 0
        while c < len(row):
            if row[c].isdigit():
                start_c = c
                num = ""
                while c < len(row) and row[c].isdigit():
                    num += row[c]
                    c += 1
                for i in range(start_c, c):
                    part_numbers[(r, i)] = int(num)
            else:
                c += 1

    for r, row in enumerate(schematic):
        for c, cell in enumerate(row):
            if cell == "*":
                adjacent_parts = set()
                for adj_x, adj_y in get_adjacent_coords(r, c, schematic):
                    if (adj_x, adj_y) in part_numbers:
                        adjacent_parts.add(part_numbers[(adj_x, adj_y)])
                        if len(adjacent_parts) > 2:
                            break

                if len(adjacent_parts) == 2:
                    total_ratio_sum += prod(adjacent_parts)

    return total_ratio_sum


def main():
    with open("input") as f:
        schematic = [line.strip() for line in f.readlines()]

    print(sum_part_numbers(schematic))
    print(sum_gear_ratios(schematic))


if __name__ == "__main__":
    main()
