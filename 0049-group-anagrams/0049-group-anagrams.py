class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        ans = []
        for s in strs:
            srt = ''.join(sorted(s))
            if srt in anagrams:
                ans[anagrams[srt]] += [s]
            else:
                anagrams[srt] = len(ans)
                ans.append([s])
        return ans
        