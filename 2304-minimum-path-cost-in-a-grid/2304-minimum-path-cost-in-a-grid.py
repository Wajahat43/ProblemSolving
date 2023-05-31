class Solution:
    #I will use dp to store the cost of reach each cell at ith row
    def minPathCost(self, grid: list[list[int]], moveCost: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        #cost of reaching previous row (0 for at the begining)
        prevRow = [0 for i in range(cols)]

        #For all rows in grid
        for row in range(1,rows):
            #list stores cost of reach each element in current row
            currentRow = [float("inf") for j in range(cols)]
            #for all elements in current row
            for col in range(cols):
                #find the minimum cost of reach jth element in current row
                #from all elements of previous row
                for pCol in range(cols):
                    prevVal = grid[row-1][pCol]
                    costs = moveCost[prevVal]
                    currentRow[col] = min(currentRow[col], costs[col]+prevVal + prevRow[pCol])
                    
            prevRow = currentRow

        #preRow now will have cost of reaching all the elements of last row
        #find the element of last row that has cost+val minimum
        #that is the answer
        minVal = float("inf")
        for i in range(len(prevRow)):
            if grid[rows-1][i] + prevRow[i] < minVal:
                minVal = grid[rows-1][i] + prevRow[i]
        return minVal
    
    
                
