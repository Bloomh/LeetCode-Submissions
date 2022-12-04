class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # store the length of the array
        n = len(nums)
        
        # keep track of the furthest index we can get to (initially 0)
        furthest = 0
        
        for i in range(n):
            # if we can get to this step
            if i <= furthest:
                # update the furthest step we can go to if (nums[i] + i) > furthest
                furthest = max(furthest, nums[i] + i)
                
                # if we can reach the end then we should return true!
                if furthest >= n - 1:
                    return True
                
            else: # if we can't get to this step, we can't reach the end – return False
                return False