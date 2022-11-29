class MinStack:

    def __init__(self):
        # use two stacks: 
        
        # one to keep track of the actual values
        self.stack = []
        
        # one to keep track of the minimum value at each point
        self.mins = []

    def push(self, val: int) -> None:
        # add the value to our stack
        self.stack.append(val)
        
        # the new minimum value is the minimum of val and the current minimum (self.getMin())
        # so add min(val, self.getMin()) to our self.mins stack
        self.mins.append(min(val, self.getMin()))           

    def pop(self) -> None:
        # remove the last minimum from our stack
        self.mins.pop()
        
        # pop and return the last value from our stack
        return self.stack.pop()

    def top(self) -> int:
        # return the last value from our stack
        return self.stack[-1]

    def getMin(self) -> int:
        # if there are no minimums then return infinity
        # this is necessary since we will call getMin() in our push method when there are no values
        if not self.mins:
            return inf
        
        # return the current minimum value
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()