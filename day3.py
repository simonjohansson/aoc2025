def find_parts(line, min_lenght):
    results = [line]
    for i in range(1, len(line)):
        results += [line[i:]]
    return filter(lambda x: len(x) >= min_lenght, results)

def sort_parts(input):
    return sorted(input, reverse=True, key=lambda s: (int(s[0])))

def _find_num(input, lenght):
    if lenght == 0:
        return ""
    next = sort_parts(find_parts(input, min_lenght=lenght))[0]
    return next[0] + _find_num(next[1:], lenght-1)

def find_num(input, lenght):
    return int(_find_num(input, lenght))

def part1(input):
    return sum([find_num(i, 2) for i in input])

def part2(input):
    return sum([find_num(i, 12) for i in input])

if __name__ == "__main__":
    input = []
    with open("data/day3.txt") as f:
        input = f.read().split("\n")

    print(part1(input))
    print(part2(input))

    # print(_find_num("818181911112111", 12))

    # print(sort_parts(find_parts("234234234234278", min_lenght=12)))