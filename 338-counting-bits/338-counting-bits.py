class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0,1]
        pP = 2
        for i in range(2,n+1):
            if i == pP*2:
                pP = i
            ans.append(ans[i-pP]+1)
        return ans