from bisect import insort
class MedianFinder:

    def __init__(self):
        self.lst = []
        self.n = 0

    def addNum(self, num: int) -> None:
        insort(self.lst, num)
        self.n += 1
        

    def findMedian(self) -> float:
        if self.n % 2:
            return self.lst[self.n//2]
        else:
            return (self.lst[self.n//2-1] + self.lst[self.n//2])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()