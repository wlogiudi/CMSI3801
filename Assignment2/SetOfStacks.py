class SetOfStacks:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity should be greater than zero.")
        self.capacity = capacity
        self.stacks = [[]]  # Start with one stack

    def push(self, value):
        if len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([])  # Create a new stack if current one is at capacity
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            raise IndexError("Stack is empty")

        value = self.stacks[-1].pop()
        if not self.stacks[-1]:  # If the current stack is empty, remove it
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Invalid stack index")

        value = self.stacks[index].pop()
        if not self.stacks[index]:  # If the stack becomes empty, remove it
            self.stacks.pop(index)
        return value

# Example usage:
stack = SetOfStacks(3)  # Threshold for each sub-stack is 3

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.pop())  # Output: 5 (Last element pushed)
print(stack.pop_at(0))  # Output: 3 (Element popped from the first sub-stack)
