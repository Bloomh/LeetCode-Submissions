class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1,len(strs)):
                try:
                    if strs[i][j]!=char:
                        return pref
                except:
                    return pref
            pref += char
        return pref