class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set([i for i in range(len(nums)+1)])-set(nums)).pop()