class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)
        while l<r:
            m = l+(r-l)//2
            e = nums[m][0]
            if e == target:
                return m
            elif e>target:
                r = m
            else:
                l = m+1
        return l
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inside = []
        lft = newInterval[0]
        rght = newInterval[1]
        for i in intervals:
            if i[0]<=newInterval[0]<=i[1] or i[0]<=newInterval[1]<=i[1] or newInterval[0]<=i[0]<=newInterval[1] or newInterval[0]<=i[1]<=newInterval[1] :
                inside.append(True)
                lft = min(lft,i[0])
                rght = max(rght,i[1])
            else:
                inside.append(False)
        c = inside.count(True)
        if c == 0:
            intervals.insert(self.search(intervals,newInterval[0]),newInterval)
        elif c == 1:
            intervals[inside.index(True)]=[lft,rght]
        else:
            j = 0
            pop = False
            for i in range(len(inside)):
                if inside[i]:
                    pop = True
                    c-=1
                    if c == 0:
                        break
                if pop:
                    intervals.pop(j)
                else:
                    j += 1
            intervals.pop(j)
            intervals.insert(j,[lft,rght])
                        
        return intervals
        
        
        