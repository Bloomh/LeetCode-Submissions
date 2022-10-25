class Solution:
    def minimumSum(self, num: int) -> int:
        smol = heapq.nsmallest(4, str(num))
        return int(smol[0]+smol[3]) + int(smol[1] + smol[2])