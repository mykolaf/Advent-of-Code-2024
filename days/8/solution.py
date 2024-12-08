from typing import Dict, List, Tuple
from itertools import combinations

class Solver:

    def __init__(self, filename: str):

        def parse_input(filename: str) -> Tuple[Dict[int, List[int]], int, int]:
            locations = {}
            with open(filename, 'r') as file:
                lines = file.readlines()
                m, n = len(lines), len(lines[0].strip())
                for i, line in enumerate(lines):
                    for j, c in enumerate(line.strip()):
                        if c == ".":
                            continue
                        if c not in locations:
                            locations[c] = []

                        locations[c].append((i, j))
            return locations, m, n

        self.antennas, self.height, self.width = parse_input(filename)

    def is_in_bounds(self, x, y) -> bool:
        return not(x < 0 or x >= self.height or y < 0 or y >= self.width)

    def solve_part1(self) -> int:
        antinodes = set()
        for char, pos in self.antennas.items():
            if char == '#':
                continue
            for l, r in combinations(pos, 2):
                dx, dy = l[0] - r[0], l[1] - r[1]

                if self.is_in_bounds(r[0] - dx, r[1] - dy):
                    antinodes.add((r[0] - dx, r[1] - dy))

                if self.is_in_bounds(l[0] + dx, l[1] + dy):
                    antinodes.add((l[0] + dx, l[1] + dy))


        return len(antinodes)


    def solve_part2(self) -> int:
        antinodes = set()
        for char, pos in self.antennas.items():
            if char == '#':
                continue
            for l, r in combinations(pos, 2):
                dx, dy = l[0] - r[0], l[1] - r[1]

                rx, ry = r
                while self.is_in_bounds(rx, ry):
                    antinodes.add((rx, ry))
                    rx, ry = rx - dx, ry - dy

                lx, ly = l
                while self.is_in_bounds(lx, ly):
                    antinodes.add((lx, ly))
                    lx, ly = lx + dx, ly + dy

        return len(antinodes)

def main():
    solver = Solver('input.txt')
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()