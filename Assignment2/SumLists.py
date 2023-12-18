class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_linked_lists_reverse_order(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next

# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example usage:
# Create linked lists representing 617 and 295
l1 = ListNode(7)
l1.next = ListNode(1)
l1.next.next = ListNode(6)

l2 = ListNode(5)
l2.next = ListNode(9)
l2.next.next = ListNode(2)

result = add_linked_lists_reverse_order(l1, l2)
print("Sum of linked lists in reverse order:")
print_linked_list(result)
