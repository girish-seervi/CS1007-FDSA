class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = TreeNode(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node)
    def _insert_recursive(self, current, new_node):
        if new_node.data < current.data:
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node)
    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)
        print()
    def _pre_order_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)
# Example usage:
bt = BinaryTree()
# Insert elements into the binary tree
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)
# Pre-order traversal
print("Pre-order traversal:")
bt.pre_order_traversal()
