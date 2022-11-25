class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0]+arr
        result = [0]*len(arr)
        stack = [(0,0)]
        for i,num in enumerate(arr):
            while stack and stack[-1][1] > num: # remove all bigger elements from the stack until we reach a smaller or equal one
                stack.pop() 
            j = stack[-1][0] # get the index of the most recent smaller one
            result[i] = result[j] + (i-j)*num # all the ones since then will have subarrays ending at this index with this as the minimum
            stack.append((i,num))
        return sum(result) % (10**9+7)