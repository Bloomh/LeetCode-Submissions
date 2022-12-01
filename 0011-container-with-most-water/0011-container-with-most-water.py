class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        
        # we will use two pointers, left and right, to search through height from both ends
        left = 0
        right = len(height)-1
        
        while left < right:
            # if the left height is bigger than the right height
            if height[left] > height[right]:
                # update the answer if the amount of water contained by these two heights is bigger
                ans = max(ans, (right-left)*height[right])
                # since the right height was smaller, let's change that pointer
                # we don't want to change the left height since it was larger
                right -= 1
            else:
                # update the answer if the amount of water contained by these two heights is bigger
                ans = max(ans, (right-left)*height[left])
                # like before, we want to increase the left pointer now and hope that it will
                # lead to a bigger height, thus leading to more water stored in the container
                left += 1
                
        return ans