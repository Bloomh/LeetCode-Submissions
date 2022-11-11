class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        add = 1 # where to add this number in the array (the number of unique elements we have seen so far)
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[add] = nums[i]
                add+=1
        return add # return the number of unique elements we have seen