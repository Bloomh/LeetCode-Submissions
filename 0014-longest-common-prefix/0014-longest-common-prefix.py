class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        prefix = ""
        for c1,c2 in zip(min(strs), max(strs)):
            if c1 == c2:
                prefix += c1
            else:
                return prefix
        return prefix