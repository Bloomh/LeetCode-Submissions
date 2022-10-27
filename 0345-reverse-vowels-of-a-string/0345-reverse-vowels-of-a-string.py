class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        vows = [char for char in s if char in vowels]
        s = list(s)
        for i,char in enumerate(s):
            if char in vowels:
                s[i] = vows.pop()
        return ''.join(s)