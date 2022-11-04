class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # store the length of the string
        n = len(s)
        # helper method to find the letterCasePermutations of s[i:]
        def perms(i):
            # we use a list to keep track of the uppercase and lowercase version of s[i]
            # if s[i] is not a letter, then s[i].upper() and s[i].lower() will both equal s[i]
            # one of the two duplicates will then get removed since we use a set (which doesn't allow for duplicates)
            upperandlower = list(set([s[i].upper(), s[i].lower()]))
            # if we are at the end of s
            if i == n-1:
                # then just return the last character (in uppercase and lowercase, if it's a letter)
                return upperandlower
            # initialize an empty answer array
            ans = []
            # get all the permutations of s[i+1:] and iterate through them
            for perm in perms(i+1):
                # if we have a separate uppercase and lowercase character to deal with then we will do this step twice, once with each version
                for char in upperandlower:
                    # add the character + the permutation to our answer array
                    ans.append(char+perm)
            # return the answer array
            return ans
        # get all the permutations of s[0:] which is the same as s
        return perms(0)
    