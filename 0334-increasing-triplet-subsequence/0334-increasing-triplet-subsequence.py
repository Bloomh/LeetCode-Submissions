class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = secondsmallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= secondsmallest:
                secondsmallest = num
            else:
                return True
        return False