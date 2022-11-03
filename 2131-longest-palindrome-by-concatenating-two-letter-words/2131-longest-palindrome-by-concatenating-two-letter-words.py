class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        s = set(words)
        extra = 0
        ans = 0
        for word in s:
            rev = word[::-1]
            if rev == word:
                if c[word]%2 == 0:
                    ans += 2*(c[word])
                else:
                    extra = 2
                    ans += 2*(c[word]-1)
            elif rev in c:
                ans += 4*min(c[word], c[rev])
            c.pop(word)
        return ans + extra