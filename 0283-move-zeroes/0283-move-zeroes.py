class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        numZeroes = 0
        for i, num in enumerate(nums):
            if num == 0:
                numZeroes += 1
            else:
                nums[i - numZeroes], nums[i] = num, nums[i - numZeroes]