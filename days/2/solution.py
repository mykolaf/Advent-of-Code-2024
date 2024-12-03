def check_falling(l,r) -> bool:
    return l > r and (l - r) in range(1,4)

def check_rising(l,r) -> bool:
    return r > l and (r - l) in range(1,4)

def skip_ith(l, ith):
    for i, n in enumerate(l):
        if i != ith:
            yield n

def is_safe(nums):
    return all(check_rising(l, r) for l, r in zip(nums, nums[1:])) or \
        all(check_falling(l, r) for l, r in zip(nums, nums[1:]))

def solve_p1(data):
    num_safe = 0

    for report in data:
        if is_safe(report):
            num_safe += 1
    return num_safe

def solve_p2(data):
    num_safe = 0

    for report in data:
        if is_safe(report):
            num_safe += 1
        else:
            for i in range(len(report)):
                skipped = list(skip_ith(report, i))
                if is_safe(skipped):
                    num_safe += 1
                    break

    return num_safe

def main():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            nums = [int(n) for n in line.strip().split()]
            data.append(nums)

    print(f"Part1 result: {solve_p1(data)}")
    print(f"Part2 result: {solve_p2(data)}")


if __name__ == "__main__":
    main()