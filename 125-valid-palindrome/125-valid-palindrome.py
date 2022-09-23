class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        l,r = 0,len(s)-1
        while l<=r:
            if not s[l]==s[r]:
                return False
            l+=1
            r-=1
        return True