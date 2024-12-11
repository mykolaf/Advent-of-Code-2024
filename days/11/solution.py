from functools import lru_cache
import math
from typing import List

def parse_input(filename: str) -> List[int]:
    with open(filename, 'r') as file:
        line = file.readline()
    return [int(i) for i in line.strip().split()]

memo = {}
def solve_part1(n, repeats) -> int:
    if (n, repeats) in memo:
        return memo[(n, repeats)]
    
    if repeats == 0:
        res = 1
    elif n == 0:
        res = solve_part1(1, repeats - 1)
    elif count_digits(n) % 2 == 0:
        l, r = split_number_math(n)
        res = solve_part1(l, repeats - 1) + solve_part1(r, repeats - 1) 
    else:
        res = solve_part1(n * 2024, repeats - 1)

    memo[(n, repeats)] = res
    return res

@lru_cache
def count_digits(n):
    if n == 0:
        return 1
    return math.floor(math.log10(abs(n))) + 1

@lru_cache
def split_number_math(n):
    total_digits = count_digits(n)
    divisor = 10 ** (total_digits // 2)

    l = n // divisor
    r = n % divisor
    
    return l, r

def main():
    data = parse_input('input.txt')

    def solve_repeats(repeats):
        return sum(solve_part1(n, repeats) for n in data)

    print(f"Part 1 result: {solve_repeats(25)}")
    print(f"Part 2 result: {solve_repeats(75)}")

if __name__ == "__main__":
    main()