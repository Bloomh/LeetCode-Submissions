class MyStack:

    def __init__(self):
        self.fwd = collections.deque()
        self.bck = collections.deque()

    def push(self, x: int) -> None:
        while self.fwd:
            self.bck.append(self.fwd.popleft())
        self.fwd.append(x)
        while self.bck:
            self.fwd.append(self.bck.popleft())

    def pop(self) -> int:
        return self.fwd.popleft()

    def top(self) -> int:
        return self.fwd[0]

    def empty(self) -> bool:
        return len(self.fwd)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()