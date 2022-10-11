class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: # can't have triplets if fewer than 3 elements
            return False
        maxOne, maxTwo = nums[-1], float('-inf') # maxOne is the max element from the right, maxTwo is the max value of nums[j] (middle element)
        for i in range(len(nums)-2,-1,-1): # go through nums in reverse
            if nums[i] < maxTwo: # found a triple!
                return True
            elif nums[i] > maxOne: # if this is the biggest element
                maxOne = nums[i] # new maxOne
            elif maxOne > nums[i] > maxTwo: # if this could go in between the elements
                maxTwo = nums[i] # it is the new second max
        return False # no triple found :(