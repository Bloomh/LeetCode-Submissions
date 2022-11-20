class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a = [0]+list(accumulate(distance))
        dist = abs(a[destination]-a[start])
        return min(dist,a[-1]-dist)