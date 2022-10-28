class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1) # keeps track of the number of times each character in s1 appears
        c2 = Counter() # sliding window in s2
        ln1 = len(s1) # length of s1 stored
        for i, char in enumerate(s2): # for every character in s2
            c2 += Counter(char) # add this character to our counter
            if i >= ln1: # if we have looked at as many elements in s2 as there are in s1
                c2 -= Counter(s2[i - ln1]) # remove the oldest one from our counter (we want the number of elements being considered from s2 to be equal to the number of elements in s1)
            if c1 == c2: # if the counters are equal we found a permutation
                return True
        return False
            