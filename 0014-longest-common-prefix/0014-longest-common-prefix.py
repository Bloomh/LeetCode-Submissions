class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # helper method to get the common prefix of two strings
        def commonPrefix(str1, str2): 
            pref = "" # start with empty prefix
            for i in range(min(len(str1), len(str2))): # stop at the end of the shorter string
                if str1[i] == str2[i]: # if characters are the same here
                    pref += str1[i] # add to the prefix
                else: # otherwise, if they are different then we need to stop
                    return pref # return the prefix
            return pref # return the prefix
        
        prefix = strs[0] # start with the first prefix
        for i in range(1, len(strs)): # for all the other indices
            prefix = commonPrefix(prefix, strs[i]) # get the common prefix with that string
        # by the end we will have gotten the longest common prefix among all strings!
        return prefix