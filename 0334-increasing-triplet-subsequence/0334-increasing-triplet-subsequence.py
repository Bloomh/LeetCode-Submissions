class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        maxOne, maxTwo = nums[-1], float('-inf')
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < maxTwo:
                return True
            elif nums[i] > maxOne:
                maxOne = nums[i]
            elif maxOne > nums[i] > maxTwo:
                maxTwo = nums[i]
        return False