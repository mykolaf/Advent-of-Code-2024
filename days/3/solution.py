import re 

def find_pairs(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = {}
    for match in re.finditer(pattern, text):
        matches[match.start()] = (int(match.group(1)), int(match.group(2)))
   
    return matches

def find_do_functions(text):
    pattern = r'(do\(\)|don\'t\(\))'
    
    matches = []
    for match in re.finditer(pattern, text):
        matches.append((match.start(), match.group(0)))
    
    return matches

def solve_p1(data):
    acc = 0
    for line in data:
        for a, b in find_pairs(line).values():
            acc += a * b
    return acc

def solve_p2(data):
    acc = 0
    enabled = 1
    for line in data:
        pairs = find_pairs(line)
        dos = find_do_functions(line)

        mul_positions = list(pairs.keys())
        mul_positions.sort()

        mul_i = 0
        for pos, command in dos:
            while mul_positions[mul_i] < pos:
                if enabled:
                    acc += pairs[mul_positions[mul_i]][0] * pairs[mul_positions[mul_i]][1]
                mul_i += 1

            enabled = 1 if command == "do()" else 0

        while mul_i <  len(mul_positions):
            if enabled:
                acc += pairs[mul_positions[mul_i]][0] * pairs[mul_positions[mul_i]][1]
            mul_i += 1

    return acc

def main():
    data = []
    with open('input.txt', 'r') as file:
        for line in file:
            data.append(line)

    print(f"Part1 result: {solve_p1(data)}")
    print(f"Part2 result: {solve_p2(data)}")


if __name__ == "__main__":
    main()