class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        ln1 = len(s1)
        for i, char in enumerate(s2):
            c2 += Counter(char)
            if i >= ln1:
                c2 -= Counter(s2[i - ln1])
            if c1 == c2:
                return True
        return False
            