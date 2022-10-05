class MyQueue:

    def __init__(self):
        self.fwd = [] #this stack will represent the front of the queue
        self.bck = [] #this stack will represent the back of the queue

    def push(self, x: int) -> None:
        self.bck.append(x) #add to the back

    def pop(self) -> int:
        self.frontToBack()
        return self.fwd.pop() #return the top element in the front

    def peek(self) -> int:
        self.frontToBack()
        return self.fwd[-1] #return the element at the front of our queue

    def empty(self) -> bool:
        return len(self.fwd)+len(self.bck)==0 #if both our stacks are empty, the queue is empty
    
    def frontToBack(self) -> None:
        if not self.fwd: #if we don't have anything at the front
            while self.bck:
                #add all elements from the back to the front
                self.fwd.append(self.bck.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()