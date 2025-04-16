class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def front(self):
        if self.head is None:
            return None
        else:
            return self.head.data
    def is_empty(self):
        if(self.head is None):
            return True
        else:
            return False
    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    def display(self):
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()
# Example usage
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.display() 