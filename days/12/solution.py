from typing import List, Tuple

class Solver:

    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, filename: str):

        def parse_input(filename: str) -> Tuple[List[Tuple[int, int]], List[int], int]:
            lines = []
            M, N = 0, 0
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                M, N = len(lines), len(lines[0]) 
            return lines, M, N

        self.lines, self.M, self.N = parse_input(filename)


    def solve_part1(self) -> int:
        score = 0

        visited = set()

        def rec(pos):
            area = 1
            perimetereter = 0
            i, j = pos
            if pos in visited:
                return 0, 0

            visited.add(pos)
            for dx, dy in  self.DIRECTIONS:
                nx, ny = i - dx, j - dy
                if (nx < 0 or nx >= self.M or ny < 0 or ny >= self.N):
                    perimetereter += 1  
                elif not (nx < 0 or nx >= self.M or ny < 0 or ny >= self.N):
                    if self.lines[nx][ny] != self.lines[i][j]:
                        perimetereter += 1     


            for dx, dy in  self.DIRECTIONS:
                nx, ny = i - dx, j - dy
                if not (nx < 0 or nx >= self.M or ny < 0 or ny >= self.N):
                    if self.lines[nx][ny] == self.lines[i][j]:
                        res = rec((nx, ny))
                        area += res[0]
                        perimetereter += res[1]

            return area, perimetereter

        for i in range(self.M):
            for j in range(self.N):
                area, perimetereter = rec((i, j))
                score += area * perimetereter

        return score
        
    def solve_part2(self):
        score = 0

        visited = set()

        for i in range(self.M):
            for j in range(self.N):
                if (i, j) in visited:
                    continue

                area = 0
                perimeter = 0
                perim = {}
                q = [(i, j)]
                while q:
                    i2, j2 = q.pop(0)
                    if (i2, j2) in visited:
                        continue
                    
                    visited.add((i2, j2))
                    area += 1

                    for dx, dy in self.DIRECTIONS:
                        ii = i2 + dx
                        jj = j2 + dy

                        if (0 <= ii < self.M and 0 <= jj < self.N and 
                            self.lines[ii][jj] == self.lines[i2][j2]):
                            q.append((ii, jj))
                        else:
                            perimeter += 1
                            if (dx, dy) not in perim:
                                perim[(dx, dy)] = set()
                            perim[(dx, dy)].add((i2, j2))

                sides = 0
                for k, vs in perim.items():
                    visited_perim = set()
                    
                    for (pi, pj) in vs:
                        if (pi, pj) not in visited_perim:
                            sides += 1
                            q = [(pi, pj)]
                            while q:
                                i2, j2 = q.pop(0)
                                if (i2, j2) in visited_perim:
                                    continue
                                
                                visited_perim.add((i2, j2))
                                
                                for dr, dc in self.DIRECTIONS:
                                    ii, jj = i2 + dr, j2 + dc
                                    if (ii, jj) in vs:
                                        q.append((ii, jj))

                score += area * sides

        return score

def main():
    solver = Solver('input.txt')
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()