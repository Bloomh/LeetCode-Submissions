class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dist = dict(zip("abcdefghijklmnopqrstuvwxyz",distance))
        letters = {}
        for i,char in enumerate(s):
            if char in letters:
                if i-letters[char]-1 != dist[char]:
                    return False
            else:
                letters[char] = i
        return True