from itertools import chain


def parse(i):
    lines = i.split("\n")
    max_rows = len(lines) - 1
    max_cols = len(list(lines)) - 1

    grid = []
    for i in range(0, max_rows + 1):
        row = []
        for j in range(0, max_cols + 1):
            row = row + [(i, j, lines[i][j])]
        grid += [row]

    return grid, max_rows, max_cols


def find_papers(positions):
    return filter(lambda x: x[2] == "@", positions)


def find_adjacent_positions(pos, max_rows, max_cols):
    x = pos[0]
    y = pos[1]

    return filter(
        lambda adjacent: (adjacent[0] >= 0 and adjacent[1] >= 0) and adjacent[0] <= max_cols and adjacent[
            1] <= max_rows,
        [
            # Above
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),

            # Next to
            (x - 1, y),
            (x + 1, y),

            # Below
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]
    )


def find_adjecant_papers(pos, grid, max_rows, max_cols):
    return find_papers(
        [grid[adjacent[0]][adjacent[1]] for adjacent in find_adjacent_positions(pos, max_rows, max_cols)])

def find_acceccible(grid, max_rows, max_cols):
    canddiates = [
        (paper, list(find_adjecant_papers(paper, grid, max_rows, max_cols)))
        for paper in find_papers(chain.from_iterable(grid))
    ]
    return filter(lambda c: len(c[1])< 4, canddiates)

def part1(grid, max_rows, max_cols):
    return len(list(find_acceccible(grid, max_rows, max_cols)))

def _part2(grid, max_rows, max_cols, removed=[]):
    removable = list(find_acceccible(grid, max_rows, max_cols))
    if len(list(removable)) == 0:
        return removed

    new_grid = grid
    for (pos, _) in removable:
        new_grid[pos[0]][pos[1]] = (pos[0], pos[1], "x")

    return _part2(new_grid, max_rows, max_cols, removed+removable)

def part2(grid, max_rows, max_cols):
    return len(_part2(grid, max_rows, max_cols))

if __name__ == "__main__":
    i = ""
    with open("data/day4.txt") as f:
        i = f.read()

    grid, max_rows, max_cols = parse(i)
    print(part1(grid, max_rows, max_cols))
    print(part2(grid, max_rows, max_cols))