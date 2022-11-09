class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s in sums:
                return True
            sums.add(s)
        return False