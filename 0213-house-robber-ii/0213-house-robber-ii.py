class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there is only one house then just rob it
        if len(nums) == 1:
            return nums[0]
        
        def r(l, r) -> int:
            # we have 0 dollars after robbing no houses and nums[0] dollars after robbing the first house
            last_two = (0, nums[l])
            # go through the rest of the houses
            while l < r - 1:
                # add to our left pointer
                l += 1
                # if we rob this house
                rob_this_house = nums[l] + last_two[0]
                # if we dont
                dont_rob_this_house = last_two[1]
                # update the amt of money we could have gotten from the last two houses
                last_two = (last_two[1], max(rob_this_house, dont_rob_this_house))

            # return money after robbing all the houses
            return last_two[1]
        
        n = len(nums)
        return max(r(0,n-1), r(1,n))