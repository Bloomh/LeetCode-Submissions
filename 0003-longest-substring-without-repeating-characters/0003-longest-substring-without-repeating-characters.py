class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        ans = 0
        first = 0
        for i,char in enumerate(s):
            while char in s_set:
                s_set.remove(s[first])
                first += 1
            s_set.add(char)
            ans = max(ans, i - first + 1)
        return ans
            