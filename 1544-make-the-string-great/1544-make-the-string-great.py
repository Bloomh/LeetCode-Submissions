class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (s[i].upper() == s[i+1] and s[i] == s[i+1].lower()) or (s[i].lower() == s[i+1] and s[i] == s[i+1].upper()):
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
                
        return s