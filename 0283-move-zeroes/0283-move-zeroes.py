class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        z = i = 0
        while i < n - z:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                z += 1
            else:
                i += 1