class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        i = 0
        add = 0
        for num in nums:
            if num != prev:
                prev = num
                nums[add] = num
                add += 1
        return add