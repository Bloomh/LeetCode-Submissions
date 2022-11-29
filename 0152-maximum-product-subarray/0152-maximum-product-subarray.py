class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = mx = mn = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            mx, mn = max(num, num*mx, num*mn), min(num, num*mx, num*mn)
            ans = max(ans, mx)
        return ans