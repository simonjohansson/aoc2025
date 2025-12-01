import itertools
import operator
from itertools import count


def part1(ops):
    history = [('L0', 50)]
    for op in ops:
        dir, steps = op
        _, last_result = history[-1]

        operand = operator.add if dir == 'R' else operator.sub
        history = history + [(op, operand(last_result, steps) % 100)]

    return len(list(filter(lambda h: h[1] == 0, history)))


def part2(ops):
    history = [('L0', 50, 0)]
    for op in ops:
        dir, steps = op
        _, last_result, _ = history[-1]

        operand = operator.add if dir == 'R' else operator.sub

        all_steps = list(
            itertools.accumulate(
                range(0, steps),
                lambda acc, _: operand(acc, 1) % 100,
                initial=last_result
            )
        )

        new_result = all_steps[-1]

        crossed = len(list(filter(lambda x: x == 0, all_steps))) + (-1 if new_result == 0 or last_result == 0 else 0)

        history = history + [(op, new_result, crossed)]

    return sum(map(lambda x: (1 if x[1] == 0 else 0) + x[2], history))


if __name__ == "__main__":
    ops = []
    with open('data/day1.txt') as f:
        for line in f:
            ops = ops + [(line[0], int(line[1:]))]

    print(part1(ops))
    print(part2(ops))
