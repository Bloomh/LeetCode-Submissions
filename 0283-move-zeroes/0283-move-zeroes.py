class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        firstZero = 0 # index of the first zero in our growing collection of zeroes (will be our current index if we haven't yet run into any zeroes)
        for i in range(len(nums)): # for all indices in nums
            if nums[i] != 0: # if it is not a zero and we have seen a zero before (if we haven't then firstZero will be equal to i)
                nums[firstZero], nums[i] = nums[i], nums[firstZero] # swap this element and the beginning of our growing bunch of zeroes
                firstZero += 1 # index of the first zero should increase