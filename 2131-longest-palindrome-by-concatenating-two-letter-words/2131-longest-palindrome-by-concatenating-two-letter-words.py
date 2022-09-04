class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        rep = 0
        match = {}
        for i in words:
            if i in match and match[i]>0:
                match[i] -= 1
                if i[0] == i[1]:
                    rep -= 1
                ans += 4
            else:
                if i[::-1] in match:
                    match[i[::-1]]+=1
                else:
                    match[i[::-1]]=1
                if i[0]==i[1]:
                    rep += 1
        if rep>0:
            ans += 2
        return ans