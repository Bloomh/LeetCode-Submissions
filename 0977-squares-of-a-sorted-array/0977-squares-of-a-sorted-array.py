class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [num**2 for num in sorted(nums, key = abs)]