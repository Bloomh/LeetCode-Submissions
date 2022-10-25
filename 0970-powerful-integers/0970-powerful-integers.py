class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        dp = set([])
        xs = 1
        while xs <= bound:
            dp.add(xs)
            xs *= x
            if x == 1:
                break
        ans = set()
        ys = 1
        while ys <= bound:
            for num in dp:
                if num + ys <= bound:
                    ans.add(num+ys)
            ys *= y
            if y == 1:
                break
        return list(ans)
        