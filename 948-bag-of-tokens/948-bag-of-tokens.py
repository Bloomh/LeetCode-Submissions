class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r = 0,len(tokens)-1
        score = 0
        while l<=r:
            if power>=tokens[l]:
                power-=tokens[l]
                l+=1
                score += 1
            elif score>0 and l!=r:
                power += tokens[r]
                score -=1
                r-=1
            else:
                return score
        return score
        