import operator
from functools import reduce
from itertools import pairwise


def parse(input):
    parts = ([line.split() for line in input.split("\n")])
    nums = [[int(num) for num in row] for row in parts[:-1]]
    ops = parts[-1]
    l = len(ops)
    for i in range(0, l):
        yield operator.add if ops[i] == "+" else operator.mul, [line[i] for line in nums]


def parse_part2(i):
    lines = i.split("\n")
    ops = lines[-1]
    nums = lines[0:-1]

    indexes = list(i for (i, c) in enumerate(ops) if c in {'+', '*'}) + [len(ops) + 1]
    pairs = (pairwise(indexes))

    for (start, end) in pairs:
            op = ops[start:end - 1].strip()
            ns = list([n[start:end - 1] for n in nums])
            new_ns = []
            for i in range(len(ns[0]) - 1, -1, -1):
                new_ns += [(int(''.join([n[i] for n in ns])))]
            yield operator.add if op == "+" else operator.mul, new_ns


def part1(input):
    return sum([
        reduce(i[0], i[1])
        for i in input
    ])


if __name__ == "__main__":
    with open("data/day6.txt") as f:
        input = f.read()

    print(part1(parse(input)))
    print(part1(parse_part2(input)))
