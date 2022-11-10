class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefts = [1]
        rights = [1]
        for i in range(len(nums)):
            lefts.append(lefts[-1]*nums[i])
            rights.append(rights[-1]*nums[-i-1])
        rights = rights[::-1]
        return [rights[i+1]*lefts[i] for i in range(len(nums))]