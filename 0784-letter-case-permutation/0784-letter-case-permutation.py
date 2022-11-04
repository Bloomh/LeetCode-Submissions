class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        def perms(i):
            upperandlower = list(set([s[i].upper(), s[i].lower()]))
            if i == n-1:
                return upperandlower
            ans = []
            for perm in perms(i+1):
                for char in upperandlower:
                    ans.append(char+perm)
            return ans
        return perms(0)
    