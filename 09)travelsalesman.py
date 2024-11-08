from itertools import permutations
def calculate_route_distance(graph, route):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i+1]]
    distance += graph[route[-1]][route[0]]  
    return distance
def tsp(graph):
    cities = list(graph.keys())
    min_distance = float('inf')
    best_route = []

    for route in permutations(cities):
        current_distance = calculate_route_distance(graph, route)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = route

    return best_route, min_distance
graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}
route, distance = tsp(graph)
print("Shortest Route:", route)
print("Minimum Distance:", distance)
