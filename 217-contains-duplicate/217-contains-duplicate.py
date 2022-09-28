class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return collections.Counter(nums).most_common(1)[0][1]>1