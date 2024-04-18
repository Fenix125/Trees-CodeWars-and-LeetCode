class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if not node:
        return []
    all_nodes = {}
    def go_nodes(node, level=0):
        if node:
            all_nodes[node] = level
            go_nodes(node.left, level + 1)
            go_nodes(node.right, level + 1)
    go_nodes(node, level=0)
    all_nodes = sorted(all_nodes.items(), key= lambda x: x[1])
    all_nodes2 = [i.value for i, j in all_nodes]
    return all_nodes2
