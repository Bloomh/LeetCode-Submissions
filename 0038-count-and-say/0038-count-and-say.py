class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        rec = self.countAndSay(n-1)
        ans = ""
        count = 1
        for i in range(len(rec)-1):
            if rec[i] == rec[i+1]:
                count += 1
            else:
                ans += str(count) + rec[i]
                count = 1
        ans += str(count) + rec[-1]
        return ans