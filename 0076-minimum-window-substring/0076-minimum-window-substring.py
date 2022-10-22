class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t) # counter for t to check with
        window = Counter() # sliding window
        ans = "" # answer
        last = 0 # last index in our window
        for i,char in enumerate(s):
            window[char] = window.get(char,0)+1 # add this character to our window
            while window >= tCounter: # 
                if ans == "" or i - last < len(ans):
                    ans = s[last:i+1]
                window[s[last]] -= 1 # remove the last element from our counter
                last += 1
        return ans