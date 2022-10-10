class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome) # store palindrome length
        if n == 1: # no way to make 1 letter not a palindrome
            return ""
        for i, char in enumerate(palindrome): # go through palindrome
            if i == (n-1)/2 or char == "a": # if right at the center, no change makes it not a palindrome; if it is "a", we don't want to change it since it is lexicographically small
                continue
            return palindrome[:i] + "a" + palindrome[i+1:] # replace character with an "a"
        return palindrome[:-1] + "b" # if all "a", then replace the last one with a "b"