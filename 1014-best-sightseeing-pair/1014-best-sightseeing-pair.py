class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        lefts = [val+i for i,val in enumerate(values)]
        rights = [val-j for j,val in enumerate(values)]
        
        for i in range(1,len(values)):
            lefts[i] = max(lefts[i-1], lefts[i])
            rights[-i-1] = max(rights[-i-1], rights[-i])
        
        ans = 0
        for i in range(len(values)-1):
            ans = max(ans, lefts[i] + rights[i+1])
    
        return ans