class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 #this index is for t
        j = 0 #this index is for s
        n = len(s) #length of s
        m = len(t) #length of t
        while j<n and n-j<=m-i: #j<n checks that we are within s, while n-j<=m-i checks that there are more characters left to check than we have characters left to find
            if s[j] == t[i]: #if the characters we are looking at are equal
                j+=1 #we found the jth character, so we increase j by 1
            i+=1 #look at the next character in t
        return j>=n #see if we found all the characters in s