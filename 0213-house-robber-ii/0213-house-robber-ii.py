class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there is only one house then just rob it
        if len(nums) == 1:
            return nums[0]
        
        # helper method to find the maximum amount of money from robbing houses between nums[l] and nums[r-1]
        def r(l, r) -> int:
            # we have 0 dollars after robbing no houses and nums[0] dollars after robbing the first house
            last_two = (0, nums[l])
            # go through the rest of the houses
            for i in range(l+1,r):
                # if we rob this house
                rob_this_house = nums[i] + last_two[0]
                # if we dont
                dont_rob_this_house = last_two[1]
                # update the amt of money we could have gotten from the last two houses
                last_two = (last_two[1], max(rob_this_house, dont_rob_this_house))

            # return money after robbing all the houses
            return last_two[1]
        
        n = len(nums)
        # since the first and last houses are connected, let's see if it is better to rob all the houses except the last one, or all the houses except the first one
        return max(r(0,n-1), r(1,n))