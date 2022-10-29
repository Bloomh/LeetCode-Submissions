class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        times = sorted([(growTime[i], plantTime[i]) for i in range(len(plantTime))])
        ans = 0
        for (gt, pt) in times:
            ans = max(ans, gt) + pt
        return ans