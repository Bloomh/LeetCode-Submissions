class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        prefix = "" # start with empty prefix
        for chars in zip(*strs): # chars will be a tuple containing all the characters in strs index by index (we use * to unpack strs before feeding it into zip)
            if len(set(chars)) == 1: # if there is only 1 distinct character
                prefix += chars[0] # add the character to prefix
            else: # otherwise we reach an issue – return the prefix
                return prefix
        return prefix