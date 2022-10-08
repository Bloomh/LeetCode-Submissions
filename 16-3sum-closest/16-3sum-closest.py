class Solution:
    def twoSumClosest(self,nums,target):
        l, r = 0, len(nums)-1
        ans = float('inf')
        while l<r:
            total = nums[l] + nums[r]
            if total == target:
                return target
            else:
                if abs(total-target) < abs(ans - target):
                    ans = total
                if total > target:
                    r -= 1
                else:
                    l += 1
        return ans
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            last = nums.pop()
            twoClose = self.twoSumClosest(nums,target-last)
            if abs(last + twoClose - target) < abs(ans - target):
                ans = last + twoClose
            if ans == target:
                return target
        return ans