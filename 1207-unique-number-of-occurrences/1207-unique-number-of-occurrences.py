class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        s = set()
        for a in arr:
            freq[a] = freq.get(a,0)+1
            s.add(a)
        return len(s) == len(set(freq.values()))