class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        n = len(nums)
        k %= n
        reverse(0,n-1) # reverse full list
        reverse(0,k-1) # reverse first k elements (previously the last k elements)
        reverse(k,n-1) # reverse the rest of the list