directions = ['^', '>', 'v', '<']
movements = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0)
}

def solve_p1(data, M, N):
    direction = '^'
    direction_p = 0

    x, y = next(k for k, v in data.items() if v == '^')

    visited = {(x, y)}

    while True:
        if 0 > x+movements[direction][0] or M <= x+movements[direction][0] or \
            0 > y+movements[direction][1] or N <= y+movements[direction][1]:
            return len(visited)
        elif (x+movements[direction][0], y+movements[direction][1]) in data and \
              data[(x+movements[direction][0], y+movements[direction][1])] == '#':
            direction_p = (direction_p + 1) % 4
            direction = directions[direction_p]

        x, y = x+movements[direction][0], y+movements[direction][1]

        visited.add((x, y))

def solve_p2(data, M, N):
    direction = '^'
    direction_p = 0

    x, y = next(k for k, v in data.items() if v == '^')

    start_pos = (x, y)
    visited = {start_pos}

    while True:
        if 0 > x+movements[direction][0] or M <= x+movements[direction][0] or \
            0 > y+movements[direction][1] or N <= y+movements[direction][1]:
            break
        elif (x+movements[direction][0], y+movements[direction][1]) in data and \
            data[(x+movements[direction][0], y+movements[direction][1])] == '#':
            direction_p = (direction_p + 1) % 4
            direction = directions[direction_p]

        x, y = x+movements[direction][0], y+movements[direction][1]

        visited.add((x, y))

    acc = 0
    visited.remove(start_pos)

    for x1, y1 in visited:
        if (x1, y1) == start_pos:
            continue
        new_wall = (x1, y1) # new wall
        direction = '^'
        direction_p = 0
        route = {(x, y, direction)}
        x, y = next(k for k, v in data.items() if v == '^')
        route = set()
        while True:
            if 0 > x+movements[direction][0] or M <= x+movements[direction][0] or \
                0 > y+movements[direction][1] or N <= y+movements[direction][1]:
                break
            elif (x, y, direction) in route:
                acc += 1 # Loop detected
                break
            elif ((x+movements[direction][0], y+movements[direction][1]) in data and \
                data[(x+movements[direction][0], y+movements[direction][1])] == '#') or \
                 ((x+movements[direction][0], y+movements[direction][1]) == new_wall):
                direction_p = (direction_p + 1) % 4
                direction = directions[direction_p]

            route.add((x, y, direction))
            x, y = x+movements[direction][0], y+movements[direction][1]

    return acc


def main():
    data = {}
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        M, N = len(lines), len(lines[0])
        for x, line in enumerate(lines):
            for y, c in enumerate(line):
                if c != '.':
                    data[(x, y)] = c

    print(f"Part1 result: {solve_p1(data, M, N)}")
    print(f"Part2 result: {solve_p2(data, M, N)}")


if __name__ == "__main__":
    main()