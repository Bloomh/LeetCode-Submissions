class Solution:
    def search(self, nums, target):
        l,r=0,len(nums)
        while l<r:
            m = l+(r-l)//2
            e = nums[m]
            if e == target:
                return m
            elif e>target:
                r = m
            else:
                l = m+1
        return -1
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        while changed:
            el = changed.pop(0)
            srch = self.search(changed,el*2)
            if srch == -1:
                return []
            else:
                ans.append(el)
                changed.pop(srch)
        return ans