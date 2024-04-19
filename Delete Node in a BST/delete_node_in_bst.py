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
        def go_nodes(node, parent, key):
            if node:
                if node.val == key:
                    if not node.left and not node.right:
                        if parent.left == node:
                            parent.left = None
                        else:
                            parent.right = None
                    elif not node.left and node.right:
                        if parent.left == node:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    elif not node.right and node.left:
                        if parent.left == node:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    elif node.right and node.left:
                        smallest = node.right
                        while smallest.left:
                            smallest = smallest.left
                        node.val = smallest.val
                        go_nodes(node.right, node, smallest.val)
                elif node.val > key:
                    go_nodes(node.left, node, key)
                elif node.val < key:
                    go_nodes(node.right, node, key)
        dummy = TreeNode(None)
        dummy.left = root
        go_nodes(root, dummy, key)
        return dummy.left

    
root = TreeNode(5, TreeNode(3, left=TreeNode(2), right=TreeNode(4)), TreeNode(6, right=TreeNode(7)))
s = Solution()
root2 = TreeNode(5, left=TreeNode(3, left=TreeNode(2), right=TreeNode(4)), right=TreeNode(6, right=TreeNode(7)))
print(s.deleteNode(root2, 7))
        