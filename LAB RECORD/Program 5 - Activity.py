class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements) if elements else "Stack is empty"
        
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print("Stack after pushing:")
print(stack)

print("\nTop element (peek):", stack.peek())
print("\nPopped element:", stack.pop())
print("Stack after popping an element:")
print(stack)

print("\nIs the stack empty?", stack.is_empty())
print(stack)
