class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r = 0,1
        ans = 1
        n = len(s)
        if n == 0:
            return 0
        st = set([s[0]])
        while r<n:
            while s[r] in st:
                st.discard(s[l])
                l+=1
            st.add(s[r])
            r += 1
            ans = max(ans,r-l)
        return ans