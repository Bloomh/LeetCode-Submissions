class Solution(object):
    def twoSum(self, nums, target):
        seen = {} #dictionary to keep track of what values we have seen (stored as keys) and their index (stored as values)
        for i, num in enumerate(nums): #i is the index, num is the number (nums[i])
            needed = target-num #this is the amount we need to sum to target
            if needed in seen: #if we have seen this amount then we found the pair!
                return [seen[needed],i] #return the indices
            else:
                seen[num] = i #add this number and its index into the dictionary
            