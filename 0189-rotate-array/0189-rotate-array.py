class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        copy = [num for num in nums] # copy the nums array
        n = len(nums)
        for i, num in enumerate(copy): # for every element in the copy
            nums[(i + k) % n] = copy[i] # set corresponding location in nums