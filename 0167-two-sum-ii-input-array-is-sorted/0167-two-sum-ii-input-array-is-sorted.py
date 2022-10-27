class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1 # left and right pointers
        while True:  
            tot = numbers[left] + numbers[right] # sum of the elements at the two pointers
            if tot == target: # if we found the total
                return [left+1, right+1] # return the indices
            elif tot > target: # if the total is too big
                right -= 1 # make the right pointer point to a smaller element
            else: # total is too small
                left += 1 # make the left pointer point to a bigger element
        # guaranteed to have an answer so nothing we need to do here