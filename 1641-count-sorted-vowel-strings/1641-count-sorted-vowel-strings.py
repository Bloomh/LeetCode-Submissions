class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans = 1
        dp = [[1]*n]
        for i in range(4):
            dp.append([1])
            for i in range(n-1):
                dp[-1].append(dp[-1][-1]+dp[-2][i+1])
            ans += dp[-1][-1]
        return ans