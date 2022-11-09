class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        comp = list(accumulate(sorted(nums)))
        return [bisect.bisect(comp, query) for query in queries]