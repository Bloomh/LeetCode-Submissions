class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [None]*k
        self.f = -1
        self.r = -1
        self.len = 0

    def enQueue(self, value: int) -> bool:
        if self.len==self.k:
            return False
        if self.r == -1:
            self.r = 0
            self.f = 0
        else:
            self.r = (self.r+1)%self.k
        self.q[self.r] = value
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.len == 0:
            return False
        if self.f == self.r:
            self.r = -1
            self.f = -1
        else:
            self.f = (self.f+1)%self.k
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.len == 0:
            return -1
        return self.q[self.f]

    def Rear(self) -> int:
        if self.len == 0:
            return -1
        return self.q[self.r]

    def isEmpty(self) -> bool:
        return self.len==0

    def isFull(self) -> bool:
        return self.len==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()