class Solution:
    def twoSumClosest(self,nums,target):
        l, r = 0, len(nums)-1
        ans = nums[0] + nums[1]
        diff = abs(ans - target)
        while l<r:
            total = nums[l] + nums[r]
            if total == target:
                return target
            else:
                if total > target:
                    r -= 1
                    if total - target < diff:
                        ans = total
                        diff = total - target
                else:
                    l += 1
                    if target - total < diff:
                        ans = total
                        diff = target - total
        return ans
    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        diff = abs(ans - target)
        nums.sort()
        for i in range(len(nums)-2):
            last = nums.pop()
            twoClose = self.twoSumClosest(nums,target-last)
            newDiff = abs(last + twoClose - target)
            if newDiff < diff:
                ans = last + twoClose
                diff = newDiff
            if ans == target:
                return target
        return ans