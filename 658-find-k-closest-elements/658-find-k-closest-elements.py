class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr[0] > x:
            return arr[:k]
        elif arr[-1] < x:
            return arr[-k:]
        l = 0
        r = k
        closest = []
        currDist = 0
        minDist = 0
        ans = []
        for i in range(k):
            minDist += abs(arr[i]-x)
            closest.append(arr[i])
            ans.append(arr[i])
        n = len(arr)
        currDist = minDist
        while r<n:
            if arr[l] >= x:
                return ans
            closest.pop(0)
            closest.append(arr[r])
            currDist = currDist + abs(arr[r]-x) - abs(arr[l]-x)
            if currDist < minDist:
                minDist = currDist
                ans[:] = closest[:]
            l+=1
            r+=1
        return ans
        