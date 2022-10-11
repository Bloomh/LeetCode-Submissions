class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        biggest = secondbiggest = float('-inf') # nums[k] and nums[j]
        for i in range(len(nums)-1,-1,-1): # go through nums backward
            if nums[i] >= biggest: # if it is the biggest element we've seen
                biggest = nums[i] # set it to be nums[k]
            elif nums[i] >= secondbiggest: # if it is the next biggest element
                secondbiggest = nums[i] # set it to be nums[j]
            else: # if num > nums[j] we have found a triplet!
                return True
        return False # no triplet found