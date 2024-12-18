
from collections import Counter


def solve_p1(filename):
    l = []
    r = []
    with open(filename, 'r') as file:
        for line in file:
            nums = line.strip().split()
            l.append(int(nums[0]))
            r.append(int(nums[1]))

            l.sort()
            r.sort()

    return sum(abs(ri - li) for ri, li in zip(r, l))

def solve_p2(filename):
    l = []
    r = []
    with open(filename, 'r') as file:
        for line in file:
            nums = line.strip().split()
            l.append(int(nums[0]))
            r.append(int(nums[1]))

    counter = Counter(r);

    return sum(n*counter[n] for n in l)

def main():
    print(f"Example result: {solve_p1('example.txt')}")
    print(f"Part1 result: {solve_p1('input.txt')}")

    print(f"Example result: {solve_p2('example.txt')}")
    print(f"Part2 result: {solve_p2('input.txt')}")


if __name__ == "__main__":
    main()