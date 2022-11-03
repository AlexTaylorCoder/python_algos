#To reverse doubly linked list just swap prev and next refs
def doubly_linked_list(head):
    if head is None:
        return None
        
    temp = head.next 
    head.next = head.prev
    head.prev = temp

    if head.prev is None:
        return None
    return doubly_linked_list(head.prev)


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None



node1 = Node(4)
node2 = Node(32)
node3 = Node(4)
node4 = Node(512)
node5 = Node(2)
node6 = Node(235)
node7 = Node(12)
# node8 = Node(25)

node1.next = node2
node1.prev = None
node2.next = node3
node2.prev = node1
node3.next = node4
node3.prev = node2
node4.next = node5
node4.prev = node3

def call_list():
    x = doubly_linked_list(node1)
    print(x)

call_list()