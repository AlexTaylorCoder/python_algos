# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Brute force solution, not fully implemented
class Solution:
    def addTwoNumbers(self, l1, l2):
        #Create third linked linked list
        # next = None
        l3 = ListNode()
        nextVal = 0
        while l2 and l1:
            a,b = divmod(l2.val+l1.val,10)
            temp = ListNode(b+nextVal)
            nextVal = a
            l3.next = temp
            l3 = l3.next
            
            l2 = l2.next
            l1 = l1.next
        print(l3)
        # while l2:
        #     temp = l3
        #     l3 = l2
        #     l3.next = temp
        #     l2 = l2.next
        # while l1:
        #     temp = l3
        #     l3 = l1
        #     l3.next = temp
        #     l1 = l1.next
        return l3






