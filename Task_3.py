import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Creating an extended weighted graph
G = nx.Graph()
edges = [
    ("A", "B", 1),
    ("B", "C", 2),
    ("C", "D", 3),
    ("A", "C", 4),
    ("B", "D", 5),
    ("A", "E", 10),
    ("E", "F", 2),
    ("F", "G", 1),
    ("D", "G", 8),
    ("C", "F", 6),
    ("B", "F", 7)
]

# Add edges to the graph with weights
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# Implementation of Dijkstra's algorithm using a binary heap
def dijkstra(graph, start):
    # Initialize distances from start to all vertices as infinity
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    # Priority queue that stores (distance, vertex)
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip if the vertex has already been processed
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # Check all neighbors of the current vertex
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight
            # If the new path is shorter, update the distance and push to the queue
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# Run Dijkstra's algorithm
shortest_paths = dijkstra(G, "A")
print("Shortest paths from A:")
for node, dist in shortest_paths.items():
    print(f"A -> {node}: {dist}")

# Visualize the graph
pos = nx.spring_layout(G, seed=42)  # Fix node positions for consistent layout
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=16, font_family="sans-serif")

plt.axis("off")
plt.title("Weighted Graph for Dijkstra's Algorithm")
plt.show()
