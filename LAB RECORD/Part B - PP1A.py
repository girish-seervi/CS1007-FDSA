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
    def in_order_traversal(self):
        self._in_order_recursive(self.root)
    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.data, end = ", ")
            self._in_order_recursive(node.right)
    def post_order_traversal(self):
        self._post_order_recursive(self.root)
    def _post_order_recursive(self, node):
        if node:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.data, end = ", ")

bt = BinaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(20)

# Traversal results
print("In-order traversal:")
bt.in_order_traversal()
