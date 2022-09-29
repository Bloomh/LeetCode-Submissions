class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums): #i is the index, num is the corresponding number (nums[i])
            for j in range(i+1,len(nums)): #search through the rest of the array
                if num + nums[j] == target: #if we found the pair which sums up to target
                    return [i,j] #return it
            