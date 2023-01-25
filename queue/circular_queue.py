
class CircularQueue:
    def __init__(self,maxSize=4):
        self.a = [None] * maxSize
        self.maxSize = maxSize
        self.start = -1 
        self.top = -1
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        return False
    def enqueue(self,val):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start == 0
            self.a[self.top] = val
    def dequeue(self):
        start = self.start
        if self.isEmpty():
            return "Cannot deque from empty queue."
        if self.start == self.top:
            self.start = -1 
            self.top = -1
        if self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.a[start] = None
        return self.a[start]
    def __str__(self):
        output_a = []
        for i in self.a:
            output_a.append(str(i))
        return " ".join(output_a)

deque = CircularQueue()
deque.enqueue(4)
deque.enqueue(5)
deque.enqueue(5)
deque.dequeue()
deque.dequeue()




print(deque)
# print(deque.dequeue())
# print(deque.dequeue())


# print(deque)

