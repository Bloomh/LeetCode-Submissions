class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #dictionary to keep track of what values we have seen (stored as keys) and their index (stored as values)
        for i, num in enumerate(nums): #i is the index, num is the number (nums[i])
            if target-num in seen:
                return [seen[target-num],i]
            else:
                seen[num] = i
            