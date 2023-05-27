class Solution:
    #technique being used is bottom up dynamic programming.
    def uniquePaths(self, rows: int, cols: int) -> int:
        prevRow = [0]*cols

        #iterate for each row
        for i in range(rows-1,-1,-1):
            currRow = [0]*cols
            #last column has only one path (going down)
            currRow[cols-1] = 1

            for j in range(cols-2,-1,-1):
                #at jth column of current row the value 
                #is going to be sum of values towards its right and 
                #value towards its bottom (previous row)
                currRow[j] = currRow[j+1] + prevRow[j]
            
            prevRow = currRow
        
        return prevRow[0]