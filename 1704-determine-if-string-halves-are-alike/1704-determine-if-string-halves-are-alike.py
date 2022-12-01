# we will use a set to keep track of all vowels
vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']) 
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # get half the length of the string
        half = len(s)//2
        
        # difference will keep track of the number of vowels in the first half minus the number of vowels in the second half
        difference = 0
        
        # go through half of the string
        for i in range(half):
            # if the character in the first half is a vowel
            if s[i] in vowels:
                # add to the difference
                difference += 1
                
            # if the character in the second half is a vowel
            if s[i+half] in vowels:
                # subtract from the difference
                difference -= 1
        
        # if the difference is zero, then the number of vowels in the first and second half is the same!
        return difference == 0