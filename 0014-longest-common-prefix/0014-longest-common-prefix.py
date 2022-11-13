class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        prefix = "" # start with empty prefix
        minLength = min(len(s) for s in strs) # store the minimum length of the strings
        for i in range(minLength): #add until we hit the minimum length
            if len(set(s[i] for s in strs)) == 1: # if there is only 1 distinct character at this index out of all the strings
                prefix += strs[0][i] # add the character to prefix
            else: # otherwise we reach an issue – return the prefix
                return prefix
        return prefix