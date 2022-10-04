class Solution(object):
    def search(self, nums, target):
        left,right = 0,len(nums) #[left,left+1,...,right-1] is the area we are actually considering
        while left<right: #while our range exists
            mid = (left+right)//2 #middle of our range
            num = nums[mid] #number at the middle
            if num == target: #we found the integer
                return mid
            elif num > target: #number is too big so we should look at numbers in the range [left,...,mid-1]
                right = mid
            else: #number is too small so we should look at numbers in the range [mid+1,...,right-1]
                left = mid+1
        return -1 #didn't find the number