class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numUnique = 1 # keep track of the number of unique elements we have seen (starts at 1 since the first element of nums is unique)
        for i in range(1,len(nums)): # start at index 1 and go through the rest
            if nums[i] != nums[i-1]: # if this elements is not the same as the last one then it is unique
                nums[numUnique] = nums[i] # put this number into our array after the previous unique elements
                numUnique += 1 # add to the number of unique elements we have seen
        return numUnique # return the number of unique elements we have seen