class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        lft,bot,rght,top = max(ax1,bx1),max(ay1,by1),min(ax2,bx2),min(ay2,by2) # coordinates of the overlap
        area = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) # start with the area of the two rectangles
        if rght > lft and top > bot: # if the overlap is valid (has positive area)
            area -= (rght-lft)*(top-bot) # subtract its area from our result
        return area