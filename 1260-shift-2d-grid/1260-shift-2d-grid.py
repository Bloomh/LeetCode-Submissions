class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rotate(nums: List[int], k: int) -> None:
            def reverse(start, end): # helper method to reverse from start to end
                while start < end: # while there is stuff to reverse
                    nums[start], nums[end] = nums[end], nums[start] # swap the elements at the ends
                    start, end = start + 1, end - 1 # move pointers closer to each other
            n = len(nums)
            k %= n
            reverse(0,n-1) # reverse full list
            reverse(0,k-1) # reverse first k elements (previously the last k elements)
            reverse(k,n-1) # reverse the rest of the list
            
        m = len(grid)
        n = len(grid[0])
        k %= m*n
        arr = []
        for row in grid:
            arr += row
        rotate(arr,k)
        return [arr[i*n:(i+1)*n] for i in range(m)]