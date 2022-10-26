class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k != 0: # we only want to rotate the array if we need to
            if k < n//2: # if the end is less than half the size of the array
                end = nums[-k:] # store the end of the array (which will become the front)
                for i in range(n-k-1, -1, -1): # go backwards through the first n-k elements of the array
                    nums[i+k] = nums[i] # shift everything forward k spots
                nums[:k] = end # put the old end to the front
            else: # the end is bigger than the beginning so store the beginning
                beg = nums[:-k] # store the beginning!
                for i in range(n-k, n): # go forwards through the last k elements
                    nums[(i+k)%n] = nums[i] # shift them forwards k spots (to the front of the list)
                nums[k:] = beg # set the end to the beginning
                    
                