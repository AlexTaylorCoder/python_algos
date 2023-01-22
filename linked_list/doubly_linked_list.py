class Node():
    def __init__(self,val):
        self.next = None
        self.prev = None 
        self.val = val
    def __str__(self):
        return str(self.val)

class LinkedList():
    def __init__(self,val):
        self.head = Node(val)
        self.tail = Node(val)
        self.length = 1
    def get(self,index):
        if self.check_index(index) == 0:
            return "Searching at invalid position"
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur
    def remove(self,index):
        if self.check_index(index) == 1:
            self.remove_first()
        elif self.check_index(index) == -1:
            self.remove_last()
        elif self.check_index(index) == 0:
            return "Deleting at invalid position"
        else:
            node = self.prev_node(index)
            node.next = node.next.next 
            node.next.prev = node
            self.remove_length()
    def remove_first(self):
        nextNode = self.head.next
        self.head = nextNode
        self.remove_length()
    def remove_last(self):
        temp = self.tail.prev
        self.tail.prev.next = None
        self.tail = temp
        self.remove_length()
    def add_node(self,index,val):
        if self.check_index(index) == 1:
            self.prepend(val)
        elif self.check_index(index) == -1:
            self.append(val)
        elif self.check_index(index) == 0:
            return "Inserting at invalid position"
        else:
            node = self.prev_node(index)
            temp = node.next
            node.next = Node(val)
            node.next.prev = node
            node.next.next = temp
            temp.prev = node.next
            self.add_length()
    def check_index(self,index):
        if index == 0:
            return 1
        elif index == self.length - 1:
            return -1
        elif index > self.length - 1 or index < 0:
            return 0
    def prepend(self,val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        temp.prev = self.head
        self.add_length()
        return self.head.next
    def append(self,val):
        node = self.get(self.length-1)
        node.next = Node(val)
        node.next.prev = node
        self.tail = node.next
        self.add_length()
    def prev_node(self,index):
        return self.get(index-1)
    def add_length(self):
        self.length += 1
    def remove_length(self):
        self.length -= 1
    def check_length(self):
        if self.length == 0:
            return -1
    def __str__(self):
        cur = self.head
        parts = []
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        return " , ".join(parts)
    def reverse(self):
        parts = []
        cur = self.tail
        while cur:
            parts.append(str(cur.val))
            cur = cur.prev
        return " , ".join(parts)
    def __delattr__(self):
        del self.head
        del self.tail

linkedlist = LinkedList(2)
linkedlist.prepend(4)
linkedlist.append(6)
linkedlist.append(6)
linkedlist.add_node(2,5)
print(linkedlist)

linkedlist.remove(4)
print(linkedlist.reverse())
del linkedlist
print(linkedlist)
# print(linkedlist.get(3).prev)
# print(linkedlist.length)
