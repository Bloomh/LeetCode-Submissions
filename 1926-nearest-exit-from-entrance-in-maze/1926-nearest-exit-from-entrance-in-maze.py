class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze) # store the length of the maze
        n = len(maze[0]) # store the width of the maze
        
        maze[entrance[0]][entrance[1]] = '+' # set the starting spot to a wall
        queue = deque([(entrance[0],entrance[1],0)])
                
        while queue:
            i,j,steps = queue.pop()
            if steps != 0 and (i == 0 or j == 0 or i == m-1 or j == n-1):
                return steps
            else:
                steps += 1
                for (r,c) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= r < m and 0 <= c < n and maze[r][c] == '.':
                        queue.appendleft((r,c,steps))
                        maze[r][c] = '+'
        return -1
        
            