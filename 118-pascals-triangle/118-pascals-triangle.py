class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]] #answer array starts with [1]
        for i in range(1,numRows): 
            ans.append([]) #add a new row
            ans[-1].append(1) #the first element is always a 1
            for j in range(1,i):
                ans[-1].append(ans[-2][j-1]+ans[-2][j]) #add the diagonal sums above
            ans[-1].append(1) #the last element is always a 1
        return ans