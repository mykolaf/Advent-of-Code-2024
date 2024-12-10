from typing import List, Tuple

class Solver:

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, filename: str):

        def parse_input(filename: str) -> Tuple[List[Tuple[int, int]], List[int], int]:
            lines = []
            zeroes = []
            M, N = 0, 0
            with open(filename, 'r') as file:
                lines = file.readlines()
                M, N = len(lines), len(lines[0].strip()) 
                for i, line in enumerate(lines):
                    for j, c in enumerate(line.strip()):
                        if c == '0':
                            zeroes.append((i, j))
            return lines, zeroes, M, N

        self.lines, self.trailheads, self.M, self.N = parse_input(filename)


    def solve_part1(self) -> int:
        score = 0

        def rec(pos):
            i, j = pos
            if pos not in visited and self.lines[i][j] == '9':
                visited.add(pos)
                return 1
            s = 0
            for dx, dy in  self.DIRECTIONS:
                nx, ny = i - dx, j - dy
                if not (nx < 0 or nx >= self.M or ny < 0 or ny >= self.N) and (nx, ny) not in visited:
                    if self.lines[nx][ny] == str(int(self.lines[i][j])+1) and (nx, ny) not in visited:
                        s += rec((nx, ny))

            visited.add(pos)
            return s

        for trailhead in self.trailheads:
            visited = set()
            score += rec(trailhead)

        return score
    
    def solve_part2(self) -> int:
        score = 0

        def rec(pos):
            i, j = pos
            if self.lines[i][j] == '9':
                return 1
            s = 0
            for dx, dy in  self.DIRECTIONS:
                nx, ny = i - dx, j - dy
                if not (nx < 0 or nx >= self.M or ny < 0 or ny >= self.N) and (nx, ny):
                    if self.lines[nx][ny] == str(int(self.lines[i][j])+1) and (nx, ny):
                        s += rec((nx, ny))

            return s

        for trailhead in self.trailheads:
            score += rec(trailhead)

        return score


def main():
    solver = Solver('input.txt')
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()