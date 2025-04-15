class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def find_lca(self, node1, node2):
        if not self._find_node(self.root, node1) or not self._find_node(self.root, node2):
            return None
        return self._find_lca_recursive(self.root, node1, node2)
    def _find_lca_recursive(self, current, node1, node2):
        if current is None:
            return None
        if current.data == node1 or current.data == node2:
            return current.data
        left_lca = self._find_lca_recursive(current.left, node1, node2)
        right_lca = self._find_lca_recursive(current.right, node1, node2)
        if left_lca and right_lca:
            return current.data
        return left_lca if left_lca is not None else right_lca
    def _find_node(self, current, target):
        if current is None:
            return False
        if current.data == target:
            return True
        return self._find_node(current.left, target) or self._find_node(current.right, target)

bt = BinaryTree()

bt.root = TreeNode(50)
bt.root.left = TreeNode(30)
bt.root.right = TreeNode(20)
bt.root.left.left = TreeNode(40)
bt.root.left.right = TreeNode(70)
bt.root.right.left = TreeNode(60)
bt.root.right.right = TreeNode(80)

lca_value = bt.find_lca(20, 40)
print(f"LCA of nodes 20 and 40: {lca_value}")
