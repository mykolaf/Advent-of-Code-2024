from typing import Dict, List, Tuple

class Solver:
    OPERATIONS = [
        lambda a, b : a * b,
        lambda a, b : a + b
    ]

    OPERATIONS2 = [
        lambda a, b : a * b,
        lambda a, b : a + b,
        lambda a, b : int(f"{a}{b}")
    ]

    def __init__(self, equations: Dict[Tuple[int, int], str]):
        self.equations = equations

    def check1(self, target, nums, s):

        if s == target and not nums:
            return True
        elif s > target or not nums:
            return False
        
        return any(self.check1(target, nums[1:], fun(s, nums[0])) for fun in self.OPERATIONS)
    
    def check2(self, target, nums, s):

        if s == target and not nums:
            return True
        elif s > target or not nums:
            return False
        
        return any(self.check2(target, nums[1:], fun(s, nums[0])) for fun in self.OPERATIONS2)

    def solve_part1(self) -> int:
        acc = 0

        for target, nums in self.equations.items():
            if self.check1(target, nums, 0):
                acc += target

        return acc

    def solve_part2(self) -> int:
        acc = 0

        for target, nums in self.equations.items():
            if self.check2(target, nums, 0):
                acc += target

        return acc

def parse_input(filename: str) -> Dict[int, List[int]]:
    equations = {}
    with open(filename, 'r') as file:
        for line in file:
            res, nums = line.strip().split(':')
            equations[int(res)] = [int(i) for i in nums.split()]
    return equations

def main():
    equations = parse_input('input.txt')
    solver = Solver(equations)
    print(f"Part 1 result: {solver.solve_part1()}")
    print(f"Part 2 result: {solver.solve_part2()}")

if __name__ == "__main__":
    main()