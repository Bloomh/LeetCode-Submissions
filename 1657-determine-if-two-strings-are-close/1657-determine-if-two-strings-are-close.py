class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1,s1,c2,s2 = defaultdict(int),set(),defaultdict(int),set()
        for char1, char2 in zip(word1, word2):
            c1[char1] += 1
            c2[char2] += 1
            s1.add(char1)
            s2.add(char2)
        return s1 == s2 and Counter(c1.values()) == Counter(c2.values())