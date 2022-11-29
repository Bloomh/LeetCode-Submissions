class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before = 0
        for i,(s, e) in enumerate(intervals):
            if e < newInterval[0]: # if this one ends before the interval
                # add to the number of intervals which are before newInterval
                before += 1
            elif newInterval[1] < s: # if this interval starts after the newInterval then we have no more to merge
                # return the intervals before newInterval + newInterval + remaining intervals
                return intervals[:before] + [newInterval] + intervals[i:]
            else:
                # otherwise update newInterval to be as big as necessary to contain [s,e] and newInterval
                newInterval[0] = min(s, newInterval[0])
                newInterval[1] = max(e, newInterval[1])
        # if we never hit our earlier return statement then there are no intervals after newInterval
        return intervals[:before] + [newInterval]