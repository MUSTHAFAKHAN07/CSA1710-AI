import itertools

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    return total_distance

def traveling_salesman_bruteforce(graph):
    num_cities = len(graph)
    if num_cities == 0:
        return []

    all_cities = list(range(num_cities))
    shortest_path = None
    shortest_distance = float('inf')

    for path in itertools.permutations(all_cities):
        distance = calculate_total_distance(path, graph)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    return shortest_path, shortest_distance

graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 18],
    [20, 15, 0, 28],
    [21, 18, 28, 0]
]

shortest_path, shortest_distance = traveling_salesman_bruteforce(graph)
print("Shortest Path:", shortest_path)
print("Shortest Distance:", shortest_distance)
