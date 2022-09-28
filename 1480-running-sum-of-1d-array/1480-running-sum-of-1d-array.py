class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [] #array to keep track of our answer
        for i in range(len(nums)): #iterate through all the elements in nums
            runningSum = 0 #this will keep track of the running sum up to index i
            for j in range(i+1): 
                runningSum += nums[j] #sum all the elements leading up to nums[i]
            answer.append(runningSum) #add the sum to our answer array
        return answer