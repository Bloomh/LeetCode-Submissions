class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True) # sort in reverse
        for i in range(len(nums)-2): # go through all but the last two elements
            if nums[i] < nums[i+1] + nums[i+2]: # if we can make a triangle (smaller two sides combine to be longer than the biggest side)
                return nums[i] + nums[i+1] + nums[i+2] # return the perimeter
        return 0 # no triangle possible