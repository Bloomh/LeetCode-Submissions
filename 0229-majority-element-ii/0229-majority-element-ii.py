class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        most_common = counter.most_common(2)
        ans = []
        for (key,val) in most_common:
            if val > n/3:
                ans.append(key)
        return ans