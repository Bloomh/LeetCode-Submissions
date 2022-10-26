class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: #target can't be in an empty list
            return -1
        mid = len(nums)//2 #middle of the list
        num = nums[mid] #number at the middle
        if num == target: #we found the target!
            return mid
        elif num > target: #number is too big --> search the left part of the list
            return self.search(nums[:mid],target)
        else: #number is too small --> search the right of the list
            srch = self.search(nums[mid+1:],target)
            if srch == -1: #if the element wasn't found
                return -1 #keep that result
            return mid+1+srch #since the list passed into the new method doesn't have the first mid+1 elements, we need to add that back to the index