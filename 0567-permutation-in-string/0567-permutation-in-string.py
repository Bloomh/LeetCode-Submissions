class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        ln1 = len(s1)
        for i, char in enumerate(s2):
            c2 += Counter(char)
            if c1 == c2:
                return True
            if i >= ln1 - 1:
                c2[s2[i - ln1 + 1]] -= 1
        return False
            