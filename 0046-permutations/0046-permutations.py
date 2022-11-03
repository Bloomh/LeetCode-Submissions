class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]
        perms = self.permute(nums[1:])
        ans = []
        firstnum = nums[0]
        for perm in perms:
            for i in range(n):
                copy = [num for num in perm]
                copy.insert(i, firstnum)
                ans.append(copy)
        return ans