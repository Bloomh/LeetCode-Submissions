class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        s = set()
        for a in arr:
            if a not in freq:
                freq[a] = 1
                s.add(a)
            else:
                freq[a] += 1
        return len(s) == len(set(freq.values()))