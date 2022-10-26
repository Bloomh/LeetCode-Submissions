class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = abs) # sort by absolute value
        for i in range(len(nums)):
            nums[i] = nums[i]**2 # square each value
        return nums