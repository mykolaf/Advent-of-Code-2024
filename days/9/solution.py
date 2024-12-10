from typing import List, Tuple
from itertools import combinations

class Solver:

    def __init__(self, filename: str):

        def parse_input(filename: str) -> Tuple[List[Tuple[int, int]], List[int], int]:
            files = [] # (index, length, mem_idx)
            spaces = [] # (length, mem_idx)
            total_filelength = 0
            with open(filename, 'r') as file:
                line = file.readline()
                file_idx = 0
                mem_idx = 0
                for i, c in enumerate(line.strip()):
                    if i % 2:
                        spaces.append((int(c), mem_idx))
                    else:
                        files.append((file_idx, int(c), mem_idx))
                        total_filelength += int(c)
                        file_idx += 1
                    mem_idx += int(c)
            return files, spaces, total_filelength

        self.files, self.spaces, self.total_filelength = parse_input(filename)


    def solve_part1(self) -> int:
        hashsum = 0

        def pull_id(files):
            for id, length, _ in files:
                for i in range(length):
                    yield id

        pos = 0

        from_back = pull_id(self.files[::-1])

        for file, space in zip(self.files, self.spaces):
            if pos >= self.total_filelength:
                return hashsum
            
            idx, length, _ = file
            for _ in range(length):
                hashsum += pos * idx
                pos += 1
                if pos >= self.total_filelength:
                    return hashsum

            for _ in range(space[0]):
                hashsum += pos * next(from_back)
                pos += 1
                if pos >= self.total_filelength:
                    return hashsum
                
    def solve_part2(self) -> int:
        hashsum = 0

        def enumerate_reversed(l):
            return zip(range(len(l)-1, -1, -1), reversed(l))

        for i, file in enumerate_reversed(self.files):
            idx, length, file_mem_idx = file
            for j, space in enumerate(self.spaces):
                free_space, mem_idx = space
                if mem_idx >= file_mem_idx:
                    break
                if free_space >= length:
                    self.files[i] = idx, length, mem_idx
                    self.spaces[j] = (free_space - length, mem_idx + length)
                    break

        self.files.sort(key=lambda x: x[2]) # by mem_idx

        for file in self.files:
            idx, length, file_mem_idx = file
            for i in range(file_mem_idx, file_mem_idx + length):
                hashsum += i * idx

        return hashsum


def main():
    solver = Solver('input.txt')
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()