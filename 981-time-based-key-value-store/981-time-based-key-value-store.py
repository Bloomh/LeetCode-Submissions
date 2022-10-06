class TimeMap:

    
    def __init__(self):
        self.dct = {}

    def search(self, nums, target):
        l, r = 0,len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            e = nums[m][0]
            if e>target:
                r = m-1
            elif e<target:
                l = m+1
            else:
                return nums[m][1]
        return nums[l-1][1]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct:
            self.dct[key] = [(timestamp,value)]
        else:
            self.dct[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct or timestamp<self.dct[key][0][0]:
            return ""
        return self.search(self.dct[key],timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)