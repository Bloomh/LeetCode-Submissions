class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ') # split into words
        for i, word in enumerate(words): # for every word
            words[i] = word[::-1] # reverse the word
        return ' '.join(words) # rejoin the words with a space between each one