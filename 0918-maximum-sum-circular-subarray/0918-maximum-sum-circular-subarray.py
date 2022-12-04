class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def minSubArray(arr):
            for i in range(1, len(arr)):
                arr[i] = min(arr[i], arr[i-1]+arr[i])
            return min(arr)
        
        def maxSubArray(arr):
            for i in range(1, len(arr)):
                arr[i] = max(arr[i], arr[i-1]+arr[i])
            return max(arr)
        maxAns = maxSubArray(nums[:])
        minAns = sum(nums)-minSubArray(nums[:])
        return max(maxAns, minAns) if minAns else maxAns