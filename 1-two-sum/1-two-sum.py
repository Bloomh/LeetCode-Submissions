class Solution(object):
    def twoSum(self, nums, target):
        numsWithIndex = [[num,i] for i,num in enumerate(nums)] #this array will keep track of the original index of each number
        numsWithIndex.sort() #sort by the number value        
        left, right = 0, len(nums)-1 #left and right pointers at either end of the array
        while True:
            leftNum = numsWithIndex[left][0] #left number
            rightNum = numsWithIndex[right][0] #right number
            total = leftNum + rightNum #their sum
            if total == target: #if they sum to the target
                return [numsWithIndex[left][1],numsWithIndex[right][1]] #return the indices
            elif total > target: #if the sum is too big, we need to make the right number smaller
                right -= 1
            else: #if the sum is too small, we make the left number bigger
                left += 1
            