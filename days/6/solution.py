import enum
from typing import Dict, Tuple, Set

class Direction(enum.IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class MazeSolver:
    MOVEMENTS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, grid: Dict[Tuple[int, int], str]):
        self.grid = grid
        self.height = max(x for x, _ in grid) + 1
        self.width = max(y for _, y in grid) + 1
        self.start = next(pos for pos, val in grid.items() if val == '^')

    def is_out_of_bounds(self, pos: Tuple[int, int]) -> bool:
        x, y = pos
        return x < 0 or x >= self.height or y < 0 or y >= self.width

    def solve_part1(self) -> int:
        x, y = self.start
        direction = Direction.UP
        visited = {(x, y)}

        while True:
            dx, dy = self.MOVEMENTS[direction]
            next_pos = (x + dx, y + dy)

            if self.is_out_of_bounds(next_pos):
                return len(visited)

            if next_pos in self.grid and self.grid[next_pos] == '#':
                direction = Direction((direction + 1) % 4)
                continue

            x, y = next_pos
            visited.add((x, y))

    def solve_part2(self) -> int:
        obstructions = 0
        visited_positions = self._get_initial_path()
        visited_positions.remove(self.start)

        for obstruction in visited_positions:
            if obstruction == self.start:
                continue

            if self._creates_loop(obstruction):
                obstructions += 1

        return obstructions

    def _get_initial_path(self) -> Set[Tuple[int, int]]:
        x, y = self.start
        direction = Direction.UP
        visited = {(x, y)}

        while True:
            dx, dy = self.MOVEMENTS[direction]
            next_pos = (x + dx, y + dy)

            if self.is_out_of_bounds(next_pos):
                break

            if next_pos in self.grid and self.grid[next_pos] == '#':
                direction = Direction((direction + 1) % 4)
                continue

            x, y = next_pos
            visited.add((x, y))

        return visited

    def _creates_loop(self, new_wall: Tuple[int, int]) -> bool:
        x, y = self.start
        direction = Direction.UP

        visited_states = set()
        while True:
            dx, dy = self.MOVEMENTS[direction]
            next_pos = (x + dx, y + dy)

            state = (x, y, direction)
            if state in visited_states:
                return True

            if self.is_out_of_bounds(next_pos):
                break

            if (next_pos in self.grid and self.grid[next_pos] == '#') or next_pos == new_wall:
                direction = Direction((direction + 1) % 4)
                continue

            visited_states.add(state)
            x, y = next_pos

        return False

def parse_input(filename: str) -> Dict[Tuple[int, int], str]:
    grid = {}
    with open(filename, 'r') as file:
        for x, line in enumerate(file):
            for y, char in enumerate(line.strip()):
                if char != '.':
                    grid[(x, y)] = char
    return grid

def main():
    grid = parse_input('input.txt')
    solver = MazeSolver(grid)
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()