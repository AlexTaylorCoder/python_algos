from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    


#Implement iteratively and recursively
#Can memoize if pattern,, if values random cannot memoize
def treeSum_rec(tree):
    if tree is None:
        return 0
    return tree.val + treeSum(tree.left) + treeSum(tree.right)


#Need to inplement stack data structure
def treeSum_iter(head):
    stack = []
    while head:
        head = head.left
        head = head.right
        head.pop()
    






node1 = Node(4)
node2 = Node(32)
node3 = Node(4)
node4 = Node(512)
node5 = Node(2)
node6 = Node(235)
node7 = Node(12)
# node8 = Node(25)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


# print(treeSum_rec(node1))
print(treeSum_iter(node1))