class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set((c := Counter(arr)).values())) == len(c)