class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [1,1]
        for i in range(1,len(s)):
            if int(s[i])==0:
                if 1<=int(s[i-1])<=2:
                    dp.append(dp[-2])
                else:
                    return 0
            else:
                ways = dp[-1]
                if 9<int(s[i-1:i+1])<=26:
                    ways += dp[-2]
                dp.append(ways)
        return dp[-1]
            
            