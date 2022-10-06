class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color: #the color is already this one so do nothing
            return image
        m = len(image)
        n = len(image[0])
        stack = [(sr,sc)]
        while stack:
            (r,c) = stack.pop()
            image[r][c] = color
            for (row,col) in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0<=row<m and 0<=col<n and image[row][col] == start_color:
                    stack.append((row,col))
        return image
            