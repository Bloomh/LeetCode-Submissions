class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        ox1,oy1,ox2,oy2 = max(ax1,bx1),max(ay1,by1),min(ax2,bx2),min(ay2,by2) # coordinates of the overlap
        area = (ax2-ax1)*(ay2-ay1) + (bx2-bx1)*(by2-by1) # start with the area of the two rectangles
        if ox2 > ox1 and oy2 > oy1: # if the overlap is valid (has positive area)
            area -= (ox2-ox1)*(oy2-oy1) # subtract its area from our result
        return area