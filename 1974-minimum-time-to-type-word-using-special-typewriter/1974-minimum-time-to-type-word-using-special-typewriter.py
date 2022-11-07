class Solution:
    def minTimeToType(self, word: str) -> int:
        currChar = 'a'
        ans = 0
        for char in word:
            diff = abs(ord(char)-ord(currChar))
            ans += min(diff, 26-diff)+1
            currChar = char
        return ans