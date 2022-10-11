class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for (word,count) in sorted(Counter(words).most_common(), key = lambda x:(-x[1],x[0]))[:k]] 
    # Counter(words).most_common() gets us the words sorted by how common they are in the form (word, count)
    # then we sort primarily by -x[1] which means -count since we want it to sort from biggest to smallest not smallest to biggest
    # secondary sorting key is x[0], the word itself
    # then we take just the first k elements using [:k]
    # then we go through and just return the actual word for each element