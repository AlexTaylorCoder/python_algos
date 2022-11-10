class MaxHeap:
    def __init__(self):
        self.items = []
    def add(self, val):
        self.items.append(val)

        current = len(self.items) - 1
        parent = current // 2

        while self.items[current] > self.items[parent]:
            self.items[parent], self.items[current] = self.items[current], self.items[parent]
            current, parent = parent, parent // 2
        return self.items
    def delete(self,val):
        loc = self.items.index(val)
        val[loc] = val[-1]

        current = 0
        parent = (current + 1) * 2
        return self.items
        #Check children instead of parents
    def delete_index(self,index):
        return self.items.pop(index)


newHeap = MaxHeap()
print(newHeap.add(4))
print(newHeap.add(6))
print(newHeap.add(8))
print(newHeap.add(1))
# print(newHeap.delete(1))