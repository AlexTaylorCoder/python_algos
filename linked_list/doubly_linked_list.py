class Node():
    def __init__(self,val):
        self.next = None
        self.prev = None 
        self.val = val
    def __str__(self):
        return str(self.val)

class LinkedList():

    def __init__(self,val):
        self._head = Node(val)
        self._tail = Node(val)
        self._length = 1
    def get(self,index):
        if self.check_index(index) == 0:
            return "Searching at invalid position"
        else:
            cur = self._head
            for _ in range(index):
                cur = cur.next
            return cur
    def remove(self,index):
        if self._length < 1:
            return "Nothing to delete, the linked list is empty"
        elif self.check_index(index) == 1:
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
        nextNode = self._head.next
        self._head = nextNode
        self.remove_length()
    def remove_last(self):
        temp = self._tail.prev
        self._tail.prev.next = None
        self._tail = temp
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
        elif index == self._length - 1:
            return -1
        elif index > self._length - 1 or index < 0:
            return 0
    def prepend(self,val):
        temp = self._head
        self._head = Node(val)
        self._head.next = temp
        temp.prev = self._head
        self.add_length()
        return self._head.next
    def append(self,val):
        node = self.get(self._length-1)
        node.next = Node(val)
        node.next.prev = node
        self._tail = node.next
        self.add_length()
    def prev_node(self,index):
        return self.get(index-1)
    def add_length(self):
        self._length += 1
    def remove_length(self):
        self._length -= 1
    def check_length(self):
        if self._length == 0:
            return -1
    def __str__(self):
        cur = self._head
        parts = []
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        return " , ".join(parts)
    def reverse(self):
        parts = []
        cur = self._tail
        while cur:
            parts.append(str(cur.val))
            cur = cur.prev
        return " , ".join(parts)
    def __delattr__(self):
        del self._head
        del self._tail
    def __len__(self):
        return self._length
    def __eq__(self, other):
        cur = self._head
        other_cur = other._head
        while cur:
            if cur.val != other_cur.val:
                return False
            cur = cur.next
            other = other_cur.next
        return True

linkedlist = LinkedList(2)
linkedlist2 = LinkedList(4)

print(linkedlist == linkedlist2)


linkedlist.prepend(4)
linkedlist.append(6)
linkedlist.append(6)
linkedlist.add_node(2,5)

linkedlist.remove(4)

# print(linkedlist.get(3).prev)
# print(linkedlist.length)
