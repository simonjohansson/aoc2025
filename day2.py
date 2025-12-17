def check_range(r):
    str_nums = [str(i) for i in r]
    even_str_nums = filter(lambda x: len(x) % 2 == 0, str_nums)
    parts_str_nums = map(lambda x: (x[:len(x) // 2], x[len(x) // 2:]), even_str_nums)
    same = filter(lambda x: x[0] == x[1], parts_str_nums)
    result = map(lambda x: int(x[0] + x[1]), same)
    return result


def equal_partitions(n):
    s = str(n)
    n = len(s)
    result = []
    for size in range(1, n):
        if n % size == 0:
            chunks = [s[i:i + size] for i in range(0, n, size)]
            result.append(chunks)
    return result


def check_num(n):
    return any(filter(lambda x: len(set(x)) == 1, equal_partitions(n)))


def check_range_part2(r):
    return filter(check_num, r)


def part1(ranges):
    return sum([sum(nums) for nums in [check_range(r) for r in ranges]])


def part2(ranges):
    return sum([sum(x) for x in map(check_range_part2, ranges)])


if __name__ == "__main__":
    line = ""
    with open("data/day2.txt") as f:
        line = f.readline()
    nums = line.split(",")

    rs = [range(int(rs[0]), int(rs[1]) + 1) for rs in [r.split("-") for r in nums]]
    print(part1(rs))
    print(part2(rs))
