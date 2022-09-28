class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0 #keep track of the sum on the left side
        rightSum = sum(nums) #keep track of the sum on the right side
        for i in range(len(nums)):
            rightSum -= nums[i] #subtract this number from the right
            if leftSum == rightSum: #if the sums on the left and the right are equal
                return i #we found the pivot!
            leftSum += nums[i] #add this number to the left
        return -1
            
            