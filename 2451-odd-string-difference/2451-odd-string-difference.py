class Solution:
    def oddString(self, words: List[str]) -> str:
        n = len(words[0])
        diffArrs = {}
        for word in words:
            diffArr = []
            for i in range(n-1):
                diffArr.append(ord(word[i]) - ord(word[i+1]))
            t = tuple(diffArr)
            if t in diffArrs:
                diffArrs[t] += [word]
            else:
                diffArrs[t] = [word]
        return next(val[0] for key, val in diffArrs.items() if len(val) == 1)
            