class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 # left and right of the area we are considering
        while left <= right: 
            mid = left+(right-left)//2 # middle of our range
            if nums[mid] == target:
                return mid
            if nums[left] <= target < nums[mid]: # if the target is between the left and middle values then we need to search there
                right = mid - 1
            elif nums[mid] < target <= nums[right]: # if the target is between the right and middle values then we need to search there
                left = mid + 1
            else: # otherwise the target is on the side which has been affected by the rotation and is no longer sorted
                if nums[left] <= nums[mid]: # if the left side is sorted
                    left = mid + 1 # go to the right side
                else: # if the right side is sorted
                    right = mid - 1 # go to the left side
        return -1