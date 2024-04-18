class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
def pre_order(node):
    all_nodes = []
    def go_nodes(node):
        if node:
            all_nodes.append(node.data)
            go_nodes(node.left)
            go_nodes(node.right)
    go_nodes(node)
    return all_nodes


a = Node(5)
b = Node(10)
c = Node(2)
d = Node("leaf")
a.left = b
a.right = c
c.left = d
print(pre_order(a))