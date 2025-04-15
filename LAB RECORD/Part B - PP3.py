class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def find_grandchildren(self, node):
        if not node:
            return []
        grandchildren = []
        if node.left:
            grandchildren.extend(self._get_children_values(node.left))
        if node.right:
            grandchildren.extend(self._get_children_values(node.right))
            return grandchildren
    def _get_children_values(self, parent):
        children_values = []
        if parent.left:
            children_values.append(parent.left.data)
        if parent.right:
            children_values.append(parent.right.data)
        return children_values

bt = BinaryTree()

bt.root = TreeNode(50)
bt.root.left = TreeNode(30)
bt.root.right = TreeNode(70)
bt.root.left.left = TreeNode(20)
bt.root.left.right = TreeNode(40)
bt.root.right.left = TreeNode(60)
bt.root.right.right = TreeNode(80)
bt.root.left.left.left = TreeNode(15)
bt.root.left.left.right = TreeNode(25)
bt.root.left.right.left = TreeNode(35)
bt.root.left.right.right = TreeNode(45)
bt.root.right.left.left = TreeNode(65)
bt.root.right.left.right = TreeNode(75)
bt.root.right.right.left = TreeNode(85)

def find_grandchildren_values(bt, node_value):
    node = find_node(bt.root, node_value)
    if node:
        return bt.find_grandchildren(node)
    else:
        return []
def find_node(current, node_value):
    if current is None:
        return None
    if current.data == node_value:
        return current
    left_node = find_node(current.left, node_value)
    if left_node:
        return left_node
    return find_node(current.right, node_value)

print("Grandchildren of node with value 30:", find_grandchildren_values(bt, 30))
