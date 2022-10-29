class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        index = s.find(part)
        n = len(part)
        while index > -1:
            s = s[:index] + s[index+n:]
            index = s.find(part)
        return s