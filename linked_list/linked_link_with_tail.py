# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [None, None, None, None, 2, None, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(val=None)
        self.tail = Node(val=None)
        self.length = 0

    def get(self, index: int) -> int:
        cur = self.head
        for node in range(index+1):
            if cur.next == None:
                return -1
            cur = cur.next
        return cur.val
    def addAtHead(self, val: int) -> None:
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp
        self.add_length()
        return self.head.next.val
    def addAtTail(self, val: int) -> None:
        temp = self.tail.next
        self.tail.next = Node(val) 
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = self.tail.next
        self.add_length()
        return cur.next.val
    def add_length(self):
        self.length += 1
    def remove_length(self):
        self.length -= 1
    def addAtIndex(self, index: int, val: int) -> None:
        node = self.traverse_before(index)
        if not node:
            return -1
        temp = node.next
        node.next = Node(val)
        node.next.next = temp
        self.add_length()
    def deleteAtIndex(self, index: int) -> None:
        if self.length != 0:
            node = self.traverse_before(index)
            if not node:
                return -1
            temp = node.next 
            del node.next 
            if temp:
                node.next = temp.next
            else:
                node.next = None
                self.tail.next = node
            self.remove_length()
        else:
            return -1
    def traverse_before(self,index):
        if index > self.length:
            return False
        cur = self.head
        for node in range(-1,index-1):
            cur = cur.next
        return cur
    def traverse_all(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

err1 =["MyLinkedList","addAtHead","addAtIndex","addAtTail","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtIndex","addAtTail","get","get","addAtHead","addAtTail","addAtTail","get","addAtTail","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtIndex","get","addAtTail","addAtIndex","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtIndex","addAtHead","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtTail","addAtHead","deleteAtIndex","get","addAtIndex","get","addAtIndex","addAtTail","addAtTail","get","deleteAtIndex","get","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtTail","get","addAtTail","addAtIndex","addAtHead","deleteAtIndex","addAtHead","deleteAtIndex","get","get","addAtTail","addAtIndex","get","deleteAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtIndex","get","addAtTail","addAtHead","addAtIndex","get","addAtHead","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtTail","addAtHead","addAtHead","deleteAtIndex","get","addAtHead"]
err2 = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,12,90,None,None,None,35,None,None,None,None,None,None,None,54,None,None,None,None,None,96,None,None,None,None,None,None,None,None,None,None,None,91,None,43,None,None,None,11,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,89,None,None,None,None,None,None,35,95,None,None,53,None,None,None,None,None,51,None,None,None,12,None,None,None,None,None,None,75,None,None,None,None,None,8,None]

expected = [None,None,None,None,None,None,None,None,None,None,None,None,None,None,12,90,None,None,None,35,None,None,None,None,None,None,None,54,None,None,None,None,None,96,None,None,None,None,None,None,None,None,None,None,None,91,None,43,None,None,None,11,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,89,None,None,None,None,None,None,35,20,None,None,53,None,None,None,None,None,51,None,None,None,12,None,None,None,None,None,None,75,None,None,None,None,None,8,None]

indx = expected.index(20)
print(err1[indx])
print(err2[indx])