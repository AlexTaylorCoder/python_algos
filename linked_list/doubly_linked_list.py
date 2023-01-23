class Node():
    def __init__(self,val):
        self.next = None
        self.prev = None 
        self.val = val
    def __str__(self):
        return str(self.val)

class LinkedList():

    def __init__(self,val):
        node = Node(val)
        self._head = node
        self._tail = node
        self._length = 1
    def get(self,index):
        if self.check_index(index) == 0:
            return "Searching at invalid position"
        else:
            cur = self._head
            for _ in range(index):
                cur = cur.next
            return cur
    def pop(self,index):
        check = self.check_removal(index)
        if check:
            return check
        else:
            node = self.prev_node(index)
            return self.__removal(node)
    def check_removal(self,index):
        if self._length < 1:
            return "Nothing to delete, the linked list is empty"
        elif self.check_index(index) == 1:
            return self.remove_first()
        elif self.check_index(index) == -1:
            return self.remove_last()
        elif self.check_index(index) == 0:
            return "Deleting at invalid position"
        else:
            return False

    def __removal(self,node):
        node.next = node.next.next 
        node.next.prev = node
        self.__remove_length()
        return node.next
    def remove_first(self):
        nextNode = self._head.next
        self._head = nextNode
        self.__remove_length()
        return self._head
    def remove_last(self):
        temp = self._tail.prev
        self._tail.prev.next = None
        self._tail = temp
        self.__remove_length()
        return self._tail
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
            self.__add_length()
    def check_index(self,index):
        if index == 0:
            return 1
        elif index == self._length - 1:
            return -1
        elif index > self._length - 1 or index < 0:
            return 0
    #Add to beginning 0(1)
    def prepend(self,val):
        temp = self._head
        self._head = Node(val)
        self._head.next = temp
        temp.prev = self._head
        self.__add_length()
        return self._head.next
    #Add to end from tail and tail.prev 0(1)
    def append(self,val):
        last = self._tail
        last.next = Node(val)
        last.next.prev = last
        self._tail = last.next
        self.__add_length()
    #Remove by values
    def remove(self,val):    
        node = self.find(val)
        if node:
            self.__removal(node[1].prev)

            return node[0]
        else:
            return "Value not found"
    #Find position of value 
    def find(self,val):
        cur = self._head
        count = 0
        while cur:
            if cur.val == val:
                return count, cur
            cur = cur.next 
            count += 1
        return False
    #Node before, to correctly change .next values
    def prev_node(self,index):
        return self.get(index-1)
    #Add length, should only be called when adding node
    def __add_length(self):
        self._length += 1
    #Reduce length, should only be called when deleting node
    def __remove_length(self):
        self._length -= 1
    #Display values of every node
    def __str__(self):
        cur = self._head
        parts = []
        while cur:
            parts.append(str(cur.val))
            cur = cur.next
        return " , ".join(parts)
    #Display values in reverse
    def reverse(self):
        parts = []
        cur = self._tail
        while cur:
            parts.append(str(cur.val))
            cur = cur.prev
        return " , ".join(parts)
    #Swap values at index
    def swap(self,index,val):
        node = self.get(index)
        found_val = node.val
        node.val = val
        return found_val
    #Delete by removing pointers, Python garbage collection handles the rest
    def __delattr__(self):
        if self._head == None:
            return "There are no nodes."
        cur = self._head
        while cur:
            cur.prev = None
            cur = cur.next
        self._head = None
        self._tail = None
    # len(linkedlist) == linkedlist.length
    def __len__(self):
        return self._length
    # Checks if two linked lists have equal values and order
    # Can use callback here later implement
    def __eq__(self, other,cb=None):
        cur = self._head
        other_cur = other._head
        if self._length != len(other):
            return False
        while cur:
            if cur.val != other_cur.val:
                return False
            cur = cur.next
            other_cur = other_cur.next
        return True
    # Checks if linked list lists have equal order
    def same_ordered(self, other):
        #Sorting while element will be same time as sorting at end b/c binary search will take o(logn) n times. Which is same as regular time complexity. 
        #Therefore .sort() is simplest solution making it most optimal
        cur_a = []
        other_a = []
        cur = self._head
        other_cur = other._head
        if self._length != len(other):
            return False
        while cur:
            #Same elements don't need to appended because they are already equal
            if cur.val != other_cur.val:
                cur_a.append(cur.val)
                other_a.append(other_cur.val)
            cur = cur.next
            other_cur = other_cur.next
        return True if sorted(other_a) == sorted(cur_a) else False  
    #Will need to go through all nodes, save to array and then sort() then swap values time: nlogn + n space: n
    #How to sort in place? Very inefficient, time: 2^n
    def sort(self):
        cur_a = []
        cur = self._head
        while cur:
            #Same elements don't need to appended because they are already equal
            cur_a.append(cur.val)
            cur = cur.next
        cur_a.sort()
        count = 0
        cur = self._head
        while cur:
            cur.val = cur_a[count]
            cur = cur.next
            count += 1
        return cur_a
    #Calls cb on every iteration
    def map(self,cb):
        cur = self._head
        while cur:
            cur.val = cb(cur.val)
            cur = cur.next
    #If doesn't meet conditions remove
    def filter(self,cb):
        count = 0
        cur = self._head
        #More complicated implementation so won't have to loop from beginning, reduces runtime from 2^n to n, not 100% on first time complexity 
        while cur:
            if not cb(cur.val):
                check = self.check_removal(count)
                if not check:
                    self.__removal(cur.prev)
                count -= 1
            cur = cur.next
            count += 1
            print(self)
    #Need to maintain temp variable
    def reduce(self,cb):
        prev = None 
        cur = self._head
        count = 0
        while cur:
            if not cb(cur.val):
                check = self.check_removal(count)
            if not check:
                self.__removal(cur.prev)
            cur.val = cb(cur.val)
            cur = cur.next
            count += 1  

    #Sum
    def sum(self):
        count = 0
        cur = self._head
        while cur:
            count += cur.val
            cur = cur.next
        return count

        



linkedlist = LinkedList(2)
linkedlist.append(4)

linkedlist2 = LinkedList(4)
linkedlist2.append(2)
linkedlist2.append(2)
linkedlist2.append(5)
linkedlist2.append(2)
linkedlist2.prepend(3)
linkedlist2.prepend(2)



linkedlist2.filter(lambda x: x != 2)
del linkedlist2
print(linkedlist2)
