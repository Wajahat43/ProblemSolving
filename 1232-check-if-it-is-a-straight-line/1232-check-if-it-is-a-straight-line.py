class Solution:
    #If the points are on a straight line, there x difference and y difference must
    #always be same for all points
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        xDist = coordinates[1][0] - coordinates[0][0]
        yDist = coordinates[1][1]- coordinates[0][1]
        
        for i in range(1,len(coordinates)-1):
            cx = coordinates[i+1][0] - coordinates[i][0]
            cy = coordinates[i+1][1] - coordinates[i][1]
            
            if yDist*cx != xDist*cy:
                return False
            
        return True