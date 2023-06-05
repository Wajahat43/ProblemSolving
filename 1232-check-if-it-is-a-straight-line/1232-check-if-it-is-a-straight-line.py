class Solution:
    #We will use concepts of slop
    # slop is given as m = chagne in y/ change in x
    # m1 = (y1-y0)/ (x1- x0)
    # m2 = (y2 - y0) / (x2 - x0)
    #
    #
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xDist = coordinates[1][0] - coordinates[0][0]
        yDist = coordinates[1][1]- coordinates[0][1]
        
        for i in range(1,len(coordinates)-1):
            cx = coordinates[i+1][0] - coordinates[i][0]
            cy = coordinates[i+1][1] - coordinates[i][1]
            
            if yDist*cx != xDist*cy:
                return False
            
        return True