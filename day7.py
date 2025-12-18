def _part1(lines, indexes, splits=0):
    if len(lines) == 0:
        return splits

    curr_line = lines[0]

    updated_line = list(curr_line)

    new_indexes = indexes.copy()

    if '^' not in curr_line:
        for i in indexes:
            updated_line[i] = "|"
    else:
        for i in indexes:
            if curr_line[i] == "^":
                new_indexes.remove(i)
                new_indexes.add(i - 1)
                new_indexes.add(i + 1)
                updated_line[i - 1] = "|"
                updated_line[i + 1] = "|"
                splits += 1
            else:
                updated_line[i] = "|"

    print("".join(updated_line))
    if len(lines) == 0:
        return splits

    return _part1(lines[1:], new_indexes, splits)


def part1(lines, start):
    return _part1(lines, {start}, 0)

if __name__ == "__main__":
    input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    with open("data/day7.txt") as f:
        input = f.read()

    lines = input.split("\n")
    print(lines[0])
    indexOfStart = lines[0].index("S")
    print(part1(lines[1:], indexOfStart))