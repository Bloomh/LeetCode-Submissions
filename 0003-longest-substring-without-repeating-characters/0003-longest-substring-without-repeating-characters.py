class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        ans = 0
        for i,char in enumerate(s):
            while char in s_set:
                s_set.remove(s[i-len(s_set)])
            s_set.add(char)
            ans = max(ans, len(s_set))
        return ans
            