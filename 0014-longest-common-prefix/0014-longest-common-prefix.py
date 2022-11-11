class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPref(str1,str2):
            common = ""
            for i in range(min(len(str1),len(str2))):
                if str1[i] == str2[i]:
                    common+=str1[i]
                else:
                    break
            return common
        
        pref = strs.pop()
        for s in strs:
            pref = commonPref(pref,s)
        return pref