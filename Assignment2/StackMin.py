class MinStack:
    def __init__(self):
        self.stack = []  # Main stack to hold elements
        self.min_stack = []  # Auxiliary stack to keep track of minimum elements

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None

        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        return popped

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print("Current minimum:", stack.min())  # Output: 1

stack.pop()
stack.pop()

print("Current minimum:", stack.min())  # Output: 3
