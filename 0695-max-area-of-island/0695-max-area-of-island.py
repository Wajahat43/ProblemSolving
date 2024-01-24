class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i,j):
            q = Deque()
            q.append((i,j))
            neighbors = [[1,0], [0,1], [-1,0], [0,-1]]
            marked = set()
            area = 0
            while q:
                celli, cellj = q.popleft()
                grid[celli][cellj] = 0
                area += 1
                
                for ni, nj in neighbors:
                    newi, newj = celli+ni, cellj+nj
                    if newi >= 0 and newi < len(grid) and newj >= 0 and newj < len(grid[i]) and (newi, newj) not in marked and grid[newi][newj] == 1:
                        q.append((newi,newj))
                        marked.add((newi,newj))
            return area
        
        result = 0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if cell == 1:
                    result = max(result, bfs(i,j))
                    
        return result
        
        