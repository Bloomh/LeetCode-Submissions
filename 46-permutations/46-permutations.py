class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]
        ans = []
        for i in range(len(nums)):
            perms = self.permute(nums[:i]+nums[i+1:])
            for perm in perms:
                ans.append([nums[i]]+perm)
        return ans
    