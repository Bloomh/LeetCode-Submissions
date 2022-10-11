class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) >= 2:
            newStone = stones.pop() - stones.pop()
            if newStone:
                bisect.insort(stones,newStone)
        return stones[0] if stones else 0