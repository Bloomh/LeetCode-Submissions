class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def comp(w1,w2):
            return sum(c1!=c2 for c1,c2 in zip(w1,w2)) <= 2
        def findit(word):
            for d in dictionary:
                if comp(word,d):
                    return True
            return False
        return [query for query in queries if findit(query)]