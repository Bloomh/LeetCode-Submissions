class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec = 0
        for num in arr:
            consec = (consec+1)*(num % 2)
            if consec == 3:
                return True
        return False