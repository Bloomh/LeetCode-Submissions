class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start, end = start+1, end-1
                
        i = 0
        n = len(s)
        while i < n:
            reverse(i, min(i+k,n)-1)
            i += 2*k
        return ''.join(s)