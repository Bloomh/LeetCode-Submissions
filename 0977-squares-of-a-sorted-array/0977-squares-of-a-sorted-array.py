class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        zeroIndex = bisect.bisect(nums, 0) # use bisect's binary search to look for 0 (could also write a binary search method to search for 0)
        neg, pos = zeroIndex-1, zeroIndex # negative pointer starts pointing before the 0, positive pointer starts pointing at it
        n = len(nums)
        result = []
        while 0 <= neg and pos < n:
            if nums[pos] <= -nums[neg]: # if the positive pointer points to a smaller or equal abs val
                result += [nums[pos]**2] # add smaller square
                pos += 1 # move forward
            else:
                result += [nums[neg]**2] # add smaller square
                neg -= 1 # move forward
        while 0 <= neg: # add all remaining negative numbers
            result += [nums[neg]**2]
            neg -= 1
        while pos < n: # add all remaining positive numbers
            result += [nums[pos]**2]
            pos += 1
        return result