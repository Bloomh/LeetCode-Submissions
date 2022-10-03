class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set() #keep track of letters already seen
        for char in s: #go to every character
            if char in letters: #if the character has already been seen, then it is the first letter to appear twice!
                return char 
            letters.add(char) #add the character to the set of letters