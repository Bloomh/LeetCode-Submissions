class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1,p2,p3):
            (x1,y1) = p1
            (x2,y2) = p2
            (x3,y3) = p3
            return abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2
        n = len(points)
        ans = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    ans = max(ans,area(points[i],points[j],points[k]))
        return ans
            