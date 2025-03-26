class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Method to append a node to the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
    
    # Method to search for a node by value
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False
    
    # Method to display the linked list
    def display(self):
        if self.head is None:
            print("The list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")

# Using Inputs
sll = SinglyLinkedList()

# Append nodes
sll.append(30)
sll.append(60)
sll.append(90)

# Search for a value in the list taking a value from the user
search_value = int(input("Enter a value to check in the list:"))
if sll.search(search_value):
    print(f"Node with value {search_value} found in the list.")
else:
    print(f"Node with value {search_value} not found in the list.")

# Display the list
print("Linked List:")
sll.display()
