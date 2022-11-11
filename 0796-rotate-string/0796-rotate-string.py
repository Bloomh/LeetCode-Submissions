class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if Counter(s) != Counter(goal):
            return False
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[1:] + s[:1]
        return False