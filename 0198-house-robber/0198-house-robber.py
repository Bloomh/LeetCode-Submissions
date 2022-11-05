class Solution:
    def rob(self, nums: List[int]) -> int:
        # helper method to find the most money we can get for robbing the first n houses
        @cache # store previous calls to this helper method
        def rob_n_houses(n):
            # if there is only one house to rob
            if n == 1:
                # rob it
                return nums[0]
            # if there are only two houses to rob
            if n == 2: 
                # rob the one with the most money
                return max(nums[0], nums[1])
            # otherwise we can either rob this house and not the previous one
            # or we can not rob this house and rob any houses before it

            # if we rob this house (nums[-1]), we can't rob nums[n-2], but we can rob any before that
            rob_this_house = nums[n-1] + rob_n_houses(n-2)
            
            # if we don't rob nums[n-1], we can rob any house before it, meaning this is the same as rob_n_houses(n-1)
            dont_rob_this_house = rob_n_houses(n-1)
            # do whatever gets us the most money
            return max(rob_this_house, dont_rob_this_house)
        # originally we can rob any of the houses
        return rob_n_houses(len(nums))
            