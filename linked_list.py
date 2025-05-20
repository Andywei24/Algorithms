class ListNode:
    def __init__(self, val:int):
        self.val : int = val
        self.next : ListNode | None = None 

# Initialize linked list: 1 -> 3 -> 2 -> 5 -> 4
# Initialize each node
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# Build references between nodes
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

def insert(n0 : ListNode , p : ListNode):
    """Insert node p after node n0 in the linked list"""
    n1 = n0.next
    p.next = n1
    n0.next = p

def remove(n0 : ListNode):
    """Remove the first node after node n0 in the linked list"""
    if not n0.next:
        return 
    # n0 -> p -> n1
    p = n0.next
    n1 = p.next
    n0.next = n1

def access(head : ListNode, index : int) -> ListNode | None:
    """Access the node at 'index' in the linked list"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head:ListNode, target:int) -> int:
    """Search for the first node with value target in the linked list"""
    index = 0
    while head:
        if head.val == target:  # head: the starting node of the linked list
            return index 
        head = head.next
        index += 1
    return -1
