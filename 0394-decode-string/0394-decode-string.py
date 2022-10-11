class Solution:
    def decodeString(self, s: str) -> str:
        if not s or s.isalpha():
            return s
        i = 0
        ans = ""
        count = 0
        while s[i].isalpha():
            ans += s[i]
            i += 1
        while s[i].isdigit():
            count = 10*count + int(s[i])
            i += 1
        j = i+2
        num = 1
        while num:
            num = num + (s[j] == "[") - (s[j] == "]")
            j += 1
        return ans + count * self.decodeString(s[i+1:j-1]) + self.decodeString(s[j:])