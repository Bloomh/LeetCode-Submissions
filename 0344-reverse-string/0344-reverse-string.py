class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2): # go halfway through the list
            s[i],s[-i-1] = s[-i-1],s[i] # swap this character and the character at the other end