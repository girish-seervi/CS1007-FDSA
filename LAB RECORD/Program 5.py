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
    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
    def is_empty(self):
        return self.top is None
    def __str__(Self):
        elements = []
        current = Self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "->".join(elements) if elements else "Stack is empty"
        
stack = Stack()

stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
print("Stack after pushing 5, 10, 15, 20:")
print(stack)

print("\nTop element (peek):", stack.peek())
print("\nPopped element:", stack.pop())
print("Stack after popping an element:")
print(stack)

print("\nIs the stack empty?", stack.is_empty())

print("\nPopped element:", stack.pop())
print("Popped element:", stack.pop())
print("Stack after popping all elements:")
print(stack)

print("\nIs the stack empty?", stack.is_empty())

print("\nAttempt to pop from empty stack:", stack.pop())
