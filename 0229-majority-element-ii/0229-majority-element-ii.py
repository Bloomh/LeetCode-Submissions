class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [key for (key,val) in Counter(nums).most_common(2) if val > len(nums)/3]