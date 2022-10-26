class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        for i,num in enumerate(nums):
            if num < 0: # negative number
                negatives = [num] + negatives # add to beginning of negatives
            else:
                positives = nums[i:]
                break
        result = []
        pos, neg = 0, 0
        n, m = len(positives), len(negatives)
        while pos < n and neg < m:
            if positives[pos] <= -negatives[neg]: # if next positive number has a smaller or equal absolute value
                result += [positives[pos]**2]
                pos += 1
            else:
                result += [negatives[neg]**2]
                neg += 1
        while pos < n: # if there are positive numbers remaining
            result += [positives[pos]**2] # add their squares
            pos += 1
        while neg < m: # if there are any negative numbers remaining
            result += [negatives[neg]**2] # add their squares
            neg += 1
        return result # return the result
                
        