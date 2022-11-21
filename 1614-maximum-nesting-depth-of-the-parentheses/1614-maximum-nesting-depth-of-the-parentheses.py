class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        depth = 0
        for char in s:
            if char == '(':
                depth += 1
                ans = max(ans,depth)
            elif char == ')':
                depth -= 1
        return ans