class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s)-1
        difference = 0
        while left < right:
            if s[left] in vowels:
                difference += 1
            if s[right] in vowels:
                difference -= 1
            left += 1
            right -= 1
        return difference == 0