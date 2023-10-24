from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  # (Missionaries on the left, Cannibals on the left, Boat on the left)
goal_state = (0, 0, 0)

# Define valid actions
valid_actions = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    m, c, b = state
    if m < 0 or c < 0 or m > 3 or c > 3 or (m != 0 and m < c) or (m != 3 and 3 - m < 3 - c):
        return False
    return True

def get_neighbors(state):
    neighbors = []
    for action in valid_actions:
        if state[2] == 1:  # Boat is on the left
            new_state = tuple(state[i] - action[i] if i < 2 else 1 - state[i] for i in range(3))
        else:  # Boat is on the right
            new_state = tuple(state[i] + action[i] if i < 2 else 1 - state[i] for i in range(3))
        if is_valid(new_state) and new_state != state:
            neighbors.append(new_state)
    return neighbors

def solve_missionaries_and_cannibals():
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [state, neighbor]
                queue.append((neighbor, new_path))

    return None

def print_solution(solution):
    if solution:
        print("Solution:")
        for state in solution:
            print(f"Missionaries: {state[0]}, Cannibals: {state[1]}, Boat: {'Left' if state[2] == 1 else 'Right'}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    solution = solve_missionaries_and_cannibals()
    print_solution(solution)


