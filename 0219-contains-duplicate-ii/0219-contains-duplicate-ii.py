class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set()
        for i,num in enumerate(nums):
            if num in s:
                return True
            if i >= k:
                s.remove(nums[i-k])
            s.add(num)
        return False