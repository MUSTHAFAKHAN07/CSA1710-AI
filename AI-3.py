from collections import deque

def water_jug_problem(capacity_x, capacity_y, target):
    visited = set()
    initial_state = (0, 0)
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        x, y = current_state

        if x == target or y == target:
            return current_state

        actions = [
            (capacity_x, y),
            (x, capacity_y),
            (0, y),
            (x, 0),
            (min(x + y, capacity_x), max(0, x + y - capacity_x)),
            (max(0, x + y - capacity_y), min(x + y, capacity_y))
        ]

        for action in actions:
            if action not in visited:
                queue.append(action)
                visited.add(action)
                
        return None 

def print_solution(solution, capacity_x, capacity_y):
    if solution:
        x, y = solution
        print("Solution:")
        print(f"Jug X: {x}/{capacity_x}")
        print(f"Jug Y: {y}/{capacity_y}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    capacity_x = 4  
    capacity_y = 3
    target = 2  

    solution = water_jug_problem(capacity_x, capacity_y, target)
    print_solution(solution, capacity_x, capacity_y)




