class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None # previous numebr
        add = 0 # where to add this number in the array (the number of unique elements we have seen so far)
        for num in nums: # go through all the numbers
            if num != prev: # if it is not equal to the previous number (it is unique)
                prev = num # update previous number
                nums[add] = num # add this to the array
                add += 1 # increment the number of unique elements we have seen
        return add # return the number of unique elements we have seen