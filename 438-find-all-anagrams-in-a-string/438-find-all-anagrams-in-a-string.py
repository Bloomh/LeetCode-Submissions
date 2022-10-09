class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = Counter(p)
        n = len(p)
        if n>len(s):
            return []
        curr = Counter(s[:n])
        ans = []
        if curr == check:
            ans.append(0)
        for i in range(n,len(s)):
            
            curr[s[i]]+=1
            if curr[s[i-n]] == 1:
                del curr[s[i-n]]
            else:
                curr[s[i-n]]-=1
            if curr==check:
                ans.append(i-n+1)

        return ans
        