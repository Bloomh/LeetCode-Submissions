class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0                   #this index is for t
        j = 0                   #this index is for s
        n = len(s)              #length of s
        m = len(t)              #length of t
        while j<n and i<m:      #check that we are within bounds for t and s
            if s[j] == t[i]:    #if the characters we are looking at are equal
                j+=1            #we found the jth character, so we increase j by 1
            i+=1                #look at the next character in t
        return j>=n             #see if we found all the characters in s