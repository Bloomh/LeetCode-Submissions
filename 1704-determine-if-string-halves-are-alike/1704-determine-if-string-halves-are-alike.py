class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # we will use a set to keep track of the 
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']) 
        half = len(s)//2
        difference = 0
        for i in range(half):
            if s[i] in vowels:
                difference += 1
            if s[i+half] in vowels:
                difference -= 1
        return difference == 0