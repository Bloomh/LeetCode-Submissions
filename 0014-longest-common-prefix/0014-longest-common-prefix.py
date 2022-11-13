class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        mn = mx = strs.pop()
        for s in strs:
            mn = min(mn,s)
            mx = max(mx,s)
        prefix = ""
        for c1,c2 in zip(mn, mx):
            if c1 == c2:
                prefix += c1
            else:
                return prefix
        return prefix