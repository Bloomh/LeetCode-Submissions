class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # helper method to get the common prefix of two strings
        def commonPrefix(str1, str2): 
            pref = "" # start with empty prefix
            for c1, c2 in zip(str1,str2): # get the characters in str1 and str2 in pairs (c1, c2)
                if c1 == c2: # if the characters are equal
                    pref += c1 # add to prefix
                else: # otherwise we need to stop
                    return pref # return prefix
            return pref # return the prefix
        
        return reduce(commonPrefix, strs)