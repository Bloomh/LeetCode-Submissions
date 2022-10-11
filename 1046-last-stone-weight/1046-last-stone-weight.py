class Solution:
    from heapq import heappush, heappop # push and pop elements while keeping them sorted
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [] # new array
        for stone in stones:
            heappush(arr,-stone) # add the negative value of the stone to the heap since it is small to big
        while len(arr) >= 2:
            newStone = heappop(arr) - heappop(arr) # collide the two smallest stones (which are really the biggest since we made them negative)
            if newStone: # if not zero
                heappush(arr,newStone) # add the new stone
        return -arr[0] if arr else 0 # if there are stones, return its true value (negative)
            