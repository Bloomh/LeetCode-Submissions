class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPref(str1,str2):
            common = ""
            for c1,c2 in zip(str1,str2):
                if c1 == c2:
                    common += c1
                else:
                    break
            return common
        pref = strs.pop()
        for s in strs:
            pref = commonPref(pref,s)
        return pref