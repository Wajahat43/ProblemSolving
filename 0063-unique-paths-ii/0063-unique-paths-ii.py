class Solution:
    #this is same as unique paths except there is path from certain cells
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0
        
        prevRow = [0]*cols
        
        #the bottom right corner
        prevRow[cols-1] = 1
        #iterate for each row
        for i in range(rows-1,-1,-1):
            currRow = [0]*cols
            #last column has only one path (the path from prevRow) or 0 if current
            #column has an obstacle in it
            currRow[cols-1] = prevRow[cols-1] if obstacleGrid[i][cols-1] == 0 else 0

            for j in range(cols-2,-1,-1):
                #at jth column of current row the value 
                #is going to be sum of values towards its right and 
                #value towards its bottom (previous row)
                
                currRow[j] = currRow[j+1] + prevRow[j] if obstacleGrid[i][j] == 0 else 0
            
            prevRow = currRow
        
        return prevRow[0]
        