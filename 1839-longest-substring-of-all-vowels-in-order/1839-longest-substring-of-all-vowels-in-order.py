class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vows = [None,'a','e','i','o','u', None] # vowels
        ln = 0 # length of our current substring
        vowPoint = 1 # pointer for vowels
        ans = 0 # answer
        for char in word:
            if char == vows[vowPoint]: # if we got the next vowel
                ln += 1 # bigger substring
                vowPoint += 1 # we can access the next vowel
            elif char == vows[vowPoint - 1]: # if this is the same as the last vowel, we can add to our substring
                ln += 1 # bigger substring
            else: # not the vowel we needed
                ln = int(char == 'a') # reset substring -- needs to reset to 1 if we start with an 'a'
                vowPoint = 1 + int(char == 'a') # reset pointer -- this needs to be at 2 if the character is 'a'
            if vowPoint == 6: # if we have all vowels
                ans = max(ans, ln) # update answer if needed
        return ans
        