import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Optional: node color for visualization
        self.id = str(uuid.uuid4())  # Unique ID for each node to avoid conflicts

def build_heap_tree(heap_list, index=0):
    if index >= len(heap_list):
        return None

    node = Node(heap_list[index])

    # Recursively build left and right subtrees
    node.left = build_heap_tree(heap_list, 2 * index + 1)
    node.right = build_heap_tree(heap_list, 2 * index + 2)

    return node

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

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Initial position for the root node
    tree = add_edges(tree, tree_root, pos)

    colors = [data['color'] for _, data in tree.nodes(data=True)]
    labels = {node_id: data['label'] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_size=12)
    plt.title("Binary Tree Visualization")
    plt.axis("off")
    plt.show()

# Example: build a tree from a binary heap
heap_list = [1, 3, 5, 7, 9, 6, 8]

# Build the tree from the heap list
heap_tree_root = build_heap_tree(heap_list)

# Visualize the tree
draw_tree(heap_tree_root)
