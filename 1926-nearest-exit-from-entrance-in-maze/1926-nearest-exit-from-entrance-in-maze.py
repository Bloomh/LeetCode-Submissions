class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        e1,e2 = entrance
        maze[e1][e2] = '+';
        queue = deque()
        
        for (r,c) in [(e1,e2-1),(e1-1,e2),(e1,e2+1),(e1+1,e2)]:
            if 0 <= r < m and 0 <= c < n and maze[r][c] == '.':
                queue.appendleft((r,c,1))
                
        while queue:
            i,j,steps = queue.pop()
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                return steps
            else:
                steps += 1
                for (r,c) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if maze[r][c] == '.':
                        queue.appendleft((r,c,steps))
                        maze[r][c] = '+'
        return -1
        
            