class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words) # keep track of how many of every word there are
        extra = 0 # we can have at most one extra word which has two of the same letter since it can go right in the middle
        ans = 0 # answer formed by matching pairs on the left and right of our string
        for word in words:
            if word in c: # if we have yet to analyze this word
                rev = word[::-1] # reverse of this word
                if rev == word: # if the word is a palindrome
                    if c[word]%2 == 0: # if there is an even amount then we pair evenly left and right
                        ans += 2*(c[word]) # 2 letters per word
                    else: # odd amount
                        extra = 2 # we can add the extra one to the middle of the string!
                        ans += 2*(c[word]-1) # the rest can be matched on the left/right
                elif rev in c: # otherwise if the reverse is in our counter
                    ans += 4*min(c[word], c[rev]) # we can pair the word and its reverse (4 characters for a successful pair)
                    c.pop(rev) # we looked at rev
                c.pop(word) # we looked at this word
        return ans + extra