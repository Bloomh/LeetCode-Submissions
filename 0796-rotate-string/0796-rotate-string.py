class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or Counter(s) != Counter(goal):
            return False
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[1:] + s[:1] # shift the first element to the end
        return False