class Solution:
    def jump(self, nums: List[int]) -> int:
        # we store the length of nums for later use
        n = len(nums)
        
        # this will keep track of the number of jumps we have taken
        numJumps = 0
        
        # we will keep track of the range of indices we can reach with two pointers
        # we can reach any index in the range [left, right] (inclusive) in numJumps steps!
        left = 0
        right = 0
        
        # while our right pointer is not at the end of nums
        while right < n - 1:
            maxIndex = right + 1
            for i in range(left, right+1):
                maxIndex = max(nums[i]+i, maxIndex)
            
            numJumps += 1
            left = right + 1
            right = maxIndex
            
        
        return numJumps