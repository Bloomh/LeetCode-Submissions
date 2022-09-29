class Solution(object):
    def binarySearch(self, nums, target): 
        #standard binary search method with slight modifications to deal with the format of [number, index]
        left,right=0,len(nums)
        while left<right:
            middle = (left+right)//2
            element = nums[middle][0] #make sure we are comparing the number to target
            if element == target:
                return nums[middle][1] #return the original index
            elif element>target:
                right = middle
            else:
                left = middle+1
        return -1
    
    def twoSum(self, nums, target):
        numsWithIndex = [[num,i] for i,num in enumerate(nums)] #this array will keep track of the original index of each number
        numsWithIndex.sort() #sort by the number value        
        for i, [num, j] in enumerate(numsWithIndex): #i is the index in numsWithIndex, num is the corresponding number, and j is the original index
            binSrchResult = self.binarySearch(numsWithIndex[i+1:],target-num) #search for target-num in the rest of the array
            if binSrchResult != -1:
                return [j,binSrchResult] #return the indices
            