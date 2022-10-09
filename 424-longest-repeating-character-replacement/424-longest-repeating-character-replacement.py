class Solution(object):
    def characterReplacement(self, s, k):
        left,right = 0,k
        substring = Counter(s[:k])
        maxCount = 0
        ans = k
        
        n = len(s)
        while right < n:
            substring[s[right]] += 1
            if substring[s[right]] > maxCount: # if this is the most common element
                maxCount = substring[s[right]]
            if ans - maxCount < k:
                ans += 1
            else:
                substring[s[left]] -= 1
                left += 1
            right += 1
            
        return ans