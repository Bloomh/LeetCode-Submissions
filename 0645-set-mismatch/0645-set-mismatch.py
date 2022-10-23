class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        mx = 0
        dupe = None
        for i, num in enumerate(nums):
            mx = max(num,mx)
            if num in s:
                dupe = num
            s.add(num)
        for i in range(1,mx+2):
            if i not in s:
                return [dupe, i]