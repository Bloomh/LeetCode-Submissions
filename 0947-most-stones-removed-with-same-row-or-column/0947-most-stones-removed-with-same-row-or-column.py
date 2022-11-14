class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # total number of stones minus the number of islands

        def removeIsland(i,j):
            ind = 0
            toRemove = []
            ind = 0
            while ind < len(stones):
                x,y = stones[ind]
                if x == i or y == j:
                    toRemove.append(stones.pop(ind))
                else:
                    ind += 1
            for stone in toRemove:
                removeIsland(*stone)
                    
        ans = len(stones)
        while stones:
            removeIsland(*stones.pop())
            ans -= 1
        return ans