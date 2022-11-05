class Solution:
    def rob(self, nums: List[int]) -> int:
        # we have 0 dollars after robbing no houses and nums[0] dollars after robbing the first house
        rob_n_houses = [0, nums[0]]
        # go through the rest of the houses
        for i in range(1, len(nums)):
            # if we rob this house
            rob_this_house = nums[i] + rob_n_houses[-2]
            # if we dont
            dont_rob_this_house = rob_n_houses[-1]
            # add the max amt of money at this point
            rob_n_houses.append(max(rob_this_house, dont_rob_this_house))
        # return money after robbing all the houses
        return rob_n_houses[-1] 
            