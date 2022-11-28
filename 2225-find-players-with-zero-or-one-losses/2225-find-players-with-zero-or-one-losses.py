class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dct = defaultdict(int) # keep track of how many times every player has lost with a dictionary
        for w,l in matches: # for each winner and loser
            dct[w] = dct[w] # the number of losses of the winner stays the same (we need this step to make sure that w will appear in dct.keys())
            dct[l] += 1 # add one loss to this player
        ans = [[],[]] # start an empty answer array
        for key,val in sorted(dct.items()): # go through the keys in sorted order so we approach the smaller ones first
            if val < 2: # if this player lost less than two times
                ans[val].append(key) # add them to the corresponding array (0th if they lost 0 times, 1st if they lost 1 time)
        return ans