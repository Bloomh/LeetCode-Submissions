class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b = mb = 0
        for i in range(len(blocks)):
            b+=blocks[i] == 'B'
            if i >= k:
                b -= blocks[i-k] == 'B'
            mb = max(mb,b)
        return k-mb