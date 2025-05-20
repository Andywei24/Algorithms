class ListNode:
    def __init__(self, val:int):
        self.val : int = val
        self.next : ListNode | None = None 

def insert(n0 : ListNode , p : ListNode):
    """Insert node p after node n0 in the linked list"""
    n1 = n0.next
    p.next = n1
    n0.next = p

def delete(p : ListNode):
    