class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in sorted(Counter(words).most_common(), key = lambda x:(-x[1],x[0]))[:k]]