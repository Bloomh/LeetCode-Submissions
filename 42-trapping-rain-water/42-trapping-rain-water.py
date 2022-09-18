class Solution:
    def trap(self, height: List[int]) -> int:
        lefts, rights = [i for i in height],[i for i in height]
        for i in range(1,len(height)):
            lefts[i] = max(lefts[i],lefts[i-1])
            rights[-i-1] = max(rights[-i-1],rights[-i])
        return sum([min(lefts[i],rights[i])-height[i] for i in range(len(height))])
