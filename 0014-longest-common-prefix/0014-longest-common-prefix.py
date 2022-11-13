class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        prefix = "" # start with empty prefix
        minLength = min(len(s) for s in strs) # store the minimum length of the strings
        for i in range(minLength): #add until we hit the minimum length
            prefix += strs[-1][i] # add the ith character from the last string (any would work)
            for s in strs: # for all the strings in strs
                if s[i] != prefix[-1]: # if the character doesn't match up
                    return prefix[:-1] # return everything but the last character in prefix
        # if we make it all the way with no issues then return the prefix
        return prefix