class Fancy:

    def __init__(self):
        self.lst = []
        self.add = 0
        self.mult = 1
        self.mod = 10**9+7
        
    def append(self, val: int) -> None:
        self.lst += [(val - self.add) * pow(self.mult, -1, self.mod)]

    def addAll(self, inc: int) -> None:
        self.add += inc

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.mod
        self.mult = (self.mult * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.lst):
            return -1
        return round(self.lst[idx]*self.mult + self.add) % self.mod


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)