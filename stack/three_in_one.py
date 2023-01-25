

class MultiStack:
    def __init__(self,stackSize=3):
        self.numberOfStacks = 3
        self.size = stackSize
        self.top = stackSize * self.numberOfStacks
        self.sizes = [0] * self.numberOfStacks
        self.stacks = [None] * self.top
    def __str__(self):
        a = []
        for ele in self.stacks:
            a.append(str(ele))
        return " ".join(a)
    def isEmpty(self,stack):
        if self.sizes[stack] == 0:
            return True 
        return False
    def isFull(self,stack):
        if self.sizes[stack] == self.size:
            return True 
        return False
    def queue(self,stack,val):
        indx = self.get_index(stack)
        if self.isFull(stack):
            return "Stack is Full!"
        self.stacks[indx] = val 
        self.sizes[stack] += 1
    def dequeue(self,stack):
        if self.isEmpty(stack):
            return "Cannot remove from empty stack"
        indx = self.get_index(stack)
        print(indx)
        self.stacks[indx] = None
        self.sizes[stack] -= 1
    def get_index(self,stack):
        if self.sizes[stack] == 0:
            indx = stack * self.size
            return indx
        else:
            indx = (stack * self.size) + (self.sizes[stack] - 1)
            return indx

        
test = MultiStack()
test.queue(0,5)
test.queue(0,5)
test.queue(1,5)
test.queue(1,5)


test.dequeue(0)
test.dequeue(1)
test.dequeue(0)




print(test)