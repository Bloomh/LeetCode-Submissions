class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i, char in enumerate(palindrome):
            if i == (n-1)/2 or char == "a":
                continue
            return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"