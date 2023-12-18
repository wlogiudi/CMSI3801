class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_middle_node(node):
    if node is None or node.next is None:
        return False  # Can't delete if node is None or it's the last node
    
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next
    return True

# Example usage:
# Create a linked list: a -> b -> c -> d -> e -> f
a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')
f = ListNode('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

node_to_delete = c  # Node c is to be deleted

delete_middle_node(node_to_delete)

# Print the updated linked list
current_node = a
while current_node:
    print(current_node.value, end=" -> ")
    current_node = current_node.next
