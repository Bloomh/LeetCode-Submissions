class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # store length of nums
        n = len(nums)
        # if only one element
        if n == 1:
            # return the one element
            return [nums]
        # get the permutations of all the elements besides the first one
        perms = self.permute(nums[1:])
        # initialize empty answer array
        ans = []
        # store the first number in the array (we will use this number a lot so storing it makes sense but is optional)
        firstnum = nums[0]
        # for every permutation in our permutations above
        for perm in perms:
            # we can add firstnum at any index in the permutation, which is of length n-1
            # therefore, it can be added at index 0, 1, ... n-1 (at the end of the list)
            for i in range(n):
                # make a copy of this permutation
                ans.append(perm[:i] + [firstnum] + perm[i:])
        return ans