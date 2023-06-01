import sys
sys.setrecursionlimit(10**6)

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        #get rows and cols
        rows= len(grid)
        cols= len(grid[0])
        #create a queue
        queue = deque()
        #create a set to see if we have already visited i and j
        visited = set()
        #all possible moves at any cell
        moves = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        #add the first cell
        if grid[0][0] == 0:
            queue.append([[0,0],1])
        #until queue is not empty
        while len(queue) != 0:
            #pop from queue
            val = queue.popleft()
            #get indexes
            i = val[0][0]
            j = val[0][1]
            #Get cost of reaching this cell
            cost = val[1]

            #if we have reached end position, return cost
            if i == rows-1 and j == cols -1:
                return cost
            #if we have not already visited i,j visit them
            if (i,j) not in visited:
                #add to set
                visited.add((i,j))
                #move in all valid possible directions
                for move in moves:
                    ii = i+move[0]
                    jj = j + move[1]
                    if ii >= 0 and ii < rows and jj >=0 and jj < cols and grid[ii][jj] == 0:
                        queue.append([[ii,jj],cost+1])
        #if we were not able to reach destination, return -1
        return -1
            



            



