class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    all_nodes2 = [i.val for i, j in all_nodes]
    return all_nodes2

class Solution:
    def deleteNode(self, root, key: int):
        copy_root = root
        def go_nodes(node, parent):
            if node:
                if node.val == key:
                    if not node.left and not node.right:
                        if parent.left.val == node.val:
                            parent.left = None
                        else:
                            parent.right = None
                    elif not node.left and node.right:
                        if parent.left.val == node.val:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    elif not node.right and node.left:
                        if parent.left.val == node.val:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    elif node.right and node.left:
                        parent_copy = node
                        biggest = node.right
                        while biggest.left:
                            parent_copy = biggest
                            biggest = biggest.left
                        node.val = biggest.val
                        go_nodes(biggest, parent_copy)
                else:
                    if node.val > key:
                        go_nodes(node.left, node)
                    elif node.val < key:
                        go_nodes(node.right, node)
        go_nodes(copy_root, copy_root)
        return tree_by_levels(copy_root)

    
root = TreeNode(5, TreeNode(3, left=TreeNode(2), right=TreeNode(4)), TreeNode(6, right=TreeNode(7)))
s = Solution()
print(s.deleteNode(root, 3))
        