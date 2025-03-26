class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CircularNode(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point to itself since it's circular
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Maintain circularity

    def delete_node(self, data):
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        prev = None

        # Case 1: If head node itself contains the data
        if current.data == data:
            if current.next == self.head:  # If it's the only node in the list
                self.head = None
            else:
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next  # Update last node's next
                self.head = self.head.next  # Move head to the next node
            return

        # Case 2: Search for the node to delete
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == data:
                prev.next = current.next  # Skip the current node
                return
            prev = current
            current = current.next

        print(f"Node with data {data} not found.")

    def traverse(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> " if current.next != self.head else "")
            current = current.next
            if current == self.head:
                break
        print()  # Newline after traversal

# Example usage:
cll = CircularLinkedList()

# Insert elements at the end
cll.insert_at_end(10)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.insert_at_end(40)

print("Circular linked list after insertions:")
cll.traverse()

# Delete a node
cll.delete_node(20)
print("\nCircular linked list after deleting 20:")
cll.traverse()

# Delete the head node
cll.delete_node(10)
print("\nCircular linked list after deleting head node 10:")
cll.traverse()
