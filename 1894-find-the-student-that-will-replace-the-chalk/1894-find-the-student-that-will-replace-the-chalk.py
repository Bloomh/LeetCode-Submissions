class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        a = list(accumulate(chalk))
        k %= a[-1]
        return bisect.bisect(a,k)