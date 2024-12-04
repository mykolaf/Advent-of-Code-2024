
def check(data, char, x, y):
    return (x, y) in data and data[(x, y)] == char

def solve_p1(data):
    acc = 0

    xses = dict(filter(lambda item: item[1] == 'X', data.items()))

    for pos, _ in xses.items():
        x, y = pos
        if (all([check(data, 'M', x+1, y), check(data, 'A', x+2, y), check(data, 'S', x+3, y)])):
            acc += 1
        if (all([check(data, 'M', x-1, y), check(data, 'A', x-2, y), check(data, 'S', x-3, y)])):
            acc += 1
        if (all([check(data, 'M', x, y+1), check(data, 'A', x, y+2), check(data, 'S', x, y+3)])):
            acc += 1
        if (all([check(data, 'M', x, y-1), check(data, 'A', x, y-2), check(data, 'S', x, y-3)])):
            acc += 1

        if (all([check(data, 'M', x+1, y+1), check(data, 'A', x+2, y+2), check(data, 'S', x+3, y+3)])):
            acc += 1
        if (all([check(data, 'M', x-1, y-1), check(data, 'A', x-2, y-2), check(data, 'S', x-3, y-3)])):
            acc += 1
        if (all([check(data, 'M', x-1, y+1), check(data, 'A', x-2, y+2), check(data, 'S', x-3, y+3)])):
            acc += 1
        if (all([check(data, 'M', x+1, y-1), check(data, 'A', x+2, y-2), check(data, 'S', x+3, y-3)])):
            acc += 1

    return acc

def solve_p2(data):
    acc = 0

    xses = dict(filter(lambda item: item[1] == 'A', data.items()))

    for pos, _ in xses.items():
        x, y = pos
        # M M A S S
        if (all([check(data, 'M', x+1, y+1), check(data, 'M', x-1, y+1), check(data, 'S', x-1, y-1), check(data, 'S', x+1, y-1)])):
            acc += 1
        # S S A M M
        if (all([check(data, 'M', x+1, y-1), check(data, 'M', x-1, y-1), check(data, 'S', x-1, y+1), check(data, 'S', x+1, y+1)])):
            acc += 1
        # S M A S M
        if (all([check(data, 'M', x+1, y+1), check(data, 'S', x-1, y+1), check(data, 'S', x-1, y-1), check(data, 'M', x+1, y-1)])):
            acc += 1
        # M S A M S
        if (all([check(data, 'S', x+1, y+1), check(data, 'M', x-1, y+1), check(data, 'M', x-1, y-1), check(data, 'S', x+1, y-1)])):
            acc += 1

    return acc

def main():
    data = {}
    with open('input.txt', 'r') as file:
        for i, line in enumerate(file):
            for j, c in enumerate(line):
                data[(i, j)] = c

    print(f"Part1 result: {solve_p1(data)}")
    print(f"Part2 result: {solve_p2(data)}")


if __name__ == "__main__":
    main()