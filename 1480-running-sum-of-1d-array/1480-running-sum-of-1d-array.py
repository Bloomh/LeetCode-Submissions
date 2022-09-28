class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum = [nums[0]] #our answer array starts with nums[0], which is the 0th running sum
        for i in range(1,len(nums)):
            runSum.append(runSum[i-1]+nums[i]) #the running sum up to index i is the sum of nums[i] and the running sum up to index i-1
        return runSum