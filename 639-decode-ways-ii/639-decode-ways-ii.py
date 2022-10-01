class Solution:
    def numDecodings(self, s: str) -> int:
        back2 = 1
        back1 = 8*(s[0] == "*")+1
        if s[0] == "0":
            return 0
        for i in range(1,len(s)):
            if s[i] == "*":
                ways = 9*back1
                if s[i-1] == "*":
                    ways += 15*back2 #11-26, except "20"
                elif s[i-1] == "2":
                    ways += 6*back2 #21-26
                elif s[i-1] == "1":
                    ways += 9*back2 #11-19
                back2,back1 = back1,ways
            elif s[i] == "0":
                if s[i-1] == "*":
                    back2,back1 = back1,2*back2
                elif 1<=int(s[i-1])<=2:
                    back2,back1 = back1,back2
                else:
                    return 0
            else:
                ways = back1
                if s[i-1] == "*":
                    ways += (1+(int(s[i])<=6))*back2
                elif 9<int(s[i-1:i+1])<=26:
                    ways += back2
                back2,back1 = back1,ways
        return back1%(10**9+7)
            