class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k != 0: # we only want to rotate the array if we need to
            end = nums[-k:] # store the end of the array (which will become the front)
            for i in range(n-k-1, -1, -1): # go backwards through the first n-k elements of the array
                nums[i+k] = nums[i] # shift everything forward k spots
            nums[:k] = end # put the old end to the front