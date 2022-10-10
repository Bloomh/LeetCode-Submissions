class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome) # store palindrome length
        if n == 1: # no way to make 1 letter not a palindrome
            return ""
        for i in range(n//2): # go through the first half of the palindrome
            if palindrome[i] != "a": # if it is not an "a" then we can make it lexicographically smaller
                return palindrome[:i] + "a" + palindrome[i+1:] # replace character with an "a"
        return palindrome[:-1] + "b" # if all "a", then replace the last one with a "b"