class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None


class LinkedListStack:
    def __init__(self,val):
        self.head = Node(val=val)
        self.length = 1
    def prepend(self,val):
        temp = self.head 
        self.head = Node(val)
        self.head.next = temp 
        self.length += 1
    def pop(self):
        if not self.isEmpty():
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp.val
        else:
            raise Exception("Cannot pop from an empty stack!")
    def __del__(self):
        self.head = None
        del self
    def peek(self):
        return self.head.val
    def isEmpty(self):
        if self.length == 0:
            return True 
        return False
    def __str__(self):
        a = []
        cur = self.head
        while cur:
            a.append(str(cur.val))
            cur = cur.next
        print(a)
        return " -> ".join(a)
    def __len__(self):
        return self.length


linkedlist = LinkedListStack(2)





