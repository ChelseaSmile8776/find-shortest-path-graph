import math
from collections import defaultdict

def find_shortest_path(graph, costs, parents):
    infinity = math.inf
    processed = set()

    def find_lowest_cost_node(costs):
        lowest_cost = infinity
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n, n_cost in neighbors.items():
            new_cost = cost + n_cost
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs)

    return {"costs": costs, "parents": parents}

def get_shortest_path(graph, costs, parents):
    path = []
    node = "fin"
    while node != "start":
        path.insert(0, node)
        node = parents[node]
    path.insert(0, "start")
    return path

graph = defaultdict(dict)

num_edges = int(input("Number of edges: "))
for _ in range(num_edges):
    node1 = input("First node: ")
    node2 = input("Second node: ")
    weight = float(input("Edge weight: "))
    graph[node1][node2] = weight

costs = defaultdict(lambda: math.inf)
parents = {}

start_node = input("Input start node: ")
fin_node = input("Input finish node: ")

costs[start_node] = 0
parents[start_node] = None

result = find_shortest_path(graph, costs, parents)
shortest_path = get_shortest_path(graph, result["costs"], result["parents"])
total_distance = result["costs"][fin_node]

print("Stortest path:", shortest_path)
print("Total distance:", total_distance)