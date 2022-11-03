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
        for perm in perms:
            for i in range(n):
                copy = [num for num in perm]
                copy.insert(i, nums[0])
                ans.append(copy)
        return ans