class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ans = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                while stack and stack[-1] <= -a:
                    if stack.pop() == -a:
                        a = 0
                        break
                if a != 0 and not stack:
                    ans.append(a)
        return ans + stack