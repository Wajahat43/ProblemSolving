class Solution:
    
    def countNegatives(self,grid: list[list[int]]) -> int:
        
        #I will use binary search to find number of negative values in a list
        def search(row,i,j):
            rowRes = 0
            while i <= j:
                mid = (i+j) //2
                if row[mid] < 0:
                    rowRes += (j-mid) + 1
                    j = mid-1
                else:
                    i = mid+1
            return rowRes
        res = 0
        for row in grid:
            res += search(row,0,len(row)-1)
        return res

                