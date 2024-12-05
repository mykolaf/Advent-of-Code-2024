
def topological_order(graph, vertices):
    visited = set()
    path = set()
    order = []
    allowed_vertices = set(vertices)

    def dfs(node):
        if node in path:
            raise ValueError("Circular dependency detected")

        if node in visited or node not in allowed_vertices:
            return
        
        path.add(node)
        
        for neighbor in graph.get(node, []):
            dfs(neighbor)
        
        path.remove(node)
        visited.add(node)
        
        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)
    
    return order[::-1]

def is_valid(rules, update):
    visited = set()
    for i in update:
        if any(p in visited for p in rules.get(i, [])):
            return False
        visited.add(i)
    return True

def solve_p1(rules, updates):
    acc = 0
    for update in updates:
        if is_valid(rules, update):
            acc += update[len(update)//2]
    return acc

def solve_p2(rules, updates):
    acc = 0
    for update in updates:
        if not is_valid(rules, update):
            ordered = topological_order(rules, update)
            acc += ordered[len(ordered)//2]
    return acc

def main():
    rules = {}
    updates = []
    with open('input.txt', 'r') as file:
        for line in file:
            if line == "\n":
                break
            a, b = line.split('|')
            a, b = int(a), int(b)
            if a not in rules:
                rules[a] = []
            rules[a].append(b)
        for line in file:
            updates.append(list(int(i) for i in line.split(',')))
        
            

    print(f"Part1 result: {solve_p1(rules, updates)}")
    print(f"Part2 result: {solve_p2(rules, updates)}")


if __name__ == "__main__":
    main()