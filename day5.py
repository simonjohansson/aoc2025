def merge_ranges(ranges):
    tuples = sorted((r.start, r.stop) for r in ranges)
    merged = []
    for start, stop in tuples:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], stop))
        else:
            merged.append((start, stop))
    return [range(s, e) for s, e in merged]

def id_in_ranges(id, ranges):
    return any(filter(lambda range: id in range, ranges))

def part1(ids, ranges):
    return len(list(filter(lambda i: id_in_ranges(i, ranges), ids)))

def part2(ranges):
    return sum([len(r) for r in ranges])


if __name__ == "__main__":
    input = ""
    with open("data/day5.txt") as f:
        input = f.read()

    rangesS, idsS = input.split("\n\n")
    ranges = [range(int(parts[0]), int(parts[1]) + 1) for parts in
              [line.split("-") for line in [lines for lines in rangesS.split("\n")]]]

    merged = merge_ranges(ranges)
    ids = [int(id) for id in idsS.split("\n")]

    print(part1(ids, merged))
    print(part2(merged))
