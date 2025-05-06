import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Optional: node color for visualization
        self.id = str(uuid.uuid4())  # Unique ID for each node to avoid conflicts

# --- Building the Heap Tree ---
def build_heap_tree(heap_list, index=0):
    if index >= len(heap_list):
        return None

    node = Node(heap_list[index])

    # Recursively build left and right subtrees
    node.left = build_heap_tree(heap_list, 2 * index + 1)
    node.right = build_heap_tree(heap_list, 2 * index + 2)

    return node

# --- Adding Edges to Graph ---
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        
        if node.left:
            graph.add_edge(node.id, node.left.id)
            lx = x - 1 / 2**layer
            pos[node.left.id] = (lx, y - 1)
            add_edges(graph, node.left, pos, x=lx, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            rx = x + 1 / 2**layer
            pos[node.right.id] = (rx, y - 1)
            add_edges(graph, node.right, pos, x=rx, y=y - 1, layer=layer + 1)
    
    return graph

# --- Tree Drawing Function ---
def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Initial position for the root node
    tree = add_edges(tree, tree_root, pos)

    # Get node colors from the passed colors dictionary (if available)
    node_colors = [colors.get(node_id, "#d3d3d3") for node_id in tree.nodes()] if colors else ['skyblue'] * len(tree.nodes())
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=node_colors, font_size=12)
    plt.title("Binary Tree Visualization")
    plt.axis("off")
    plt.show()

# --- Color Generation Based on Traversal Step ---
def generate_color(step, total_steps):
    base_color = [18, 150, 240]  # Starting color (dark blue)
    lighten_step = (255 - base_color[0]) / max(total_steps, 1)
    r = min(255, int(base_color[0] + step * lighten_step))
    g = min(255, int(base_color[1] + step * lighten_step))
    b = min(255, int(base_color[2] + step * lighten_step))
    return f'#{r:02x}{g:02x}{b:02x}'

def dfs_visualize(root, total_steps):
    visited = set()
    stack = [root]
    colors = {}
    step = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step, total_steps)  # Color based on the step
            step += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return colors

def bfs_visualize(root, total_steps):
    visited = set()
    queue = [root]
    colors = {}
    step = 0

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step, total_steps)  # Color based on the step
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return colors

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

if __name__ == '__main__':
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heap_tree_root = build_heap_tree(heap_list)

    # Calculate total number of nodes
    total_steps = count_nodes(heap_tree_root)

    # Perform DFS visualization
    dfs_colors = dfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, dfs_colors)

    # Perform BFS visualization
    bfs_colors = bfs_visualize(heap_tree_root, total_steps)
    draw_tree(heap_tree_root, bfs_colors)