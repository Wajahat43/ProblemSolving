class Solution:
    #I will use a heap to get n smallest values
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        pointsDis = []
        #For each point, find its distance and 
        #add it in the heap alongwith the point itself.
        for point in points:
            dis = math.sqrt(point[0]**2+point[1]**2)
            pointsDis.append((dis,point))
        #heapfiy the list
        heapq.heapify(pointsDis)
        
        result = []
        #find the first k points with smallest distance
        for i in range(k):
            result.append(heapq.heappop(pointsDis)[1])
        #return the result
        return result
        
            
        