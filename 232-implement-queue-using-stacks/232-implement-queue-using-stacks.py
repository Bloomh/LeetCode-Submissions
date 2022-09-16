class MyQueue:

    def __init__(self):
        self.fwd = []
        self.bck = []

    def push(self, x: int) -> None:
        self.bck.append(x)

    def pop(self) -> int:
        if not self.fwd:
            while self.bck:
                self.fwd.append(self.bck.pop())
        return self.fwd.pop()

    def peek(self) -> int:
        if not self.fwd:
            while self.bck:
                self.fwd.append(self.bck.pop())
        return self.fwd[-1]

    def empty(self) -> bool:
        return len(self.fwd)+len(self.bck)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()