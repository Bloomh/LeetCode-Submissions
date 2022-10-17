class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        n = len(arr)
        def reach(arr,start):
            if not 0 <= start < n:
                return False
            dist = arr[start]
            if dist == 0:
                return True
            ret = False
            if start-dist not in seen:
                seen.add(start)
                ret = ret or reach(arr,start-dist)
            if start+dist not in seen:
                seen.add(start)
                ret = ret or reach(arr,start+dist)
            return ret
        return arr[start] == 0 or reach(arr,start - arr[start]) or reach(arr, start + arr[start])