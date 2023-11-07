class Solution:
    #The reason is if we can find the time at which a monster will reach the city.
    #time will be distance/speed (we will ceil it)
    #Then we sort by time, and then start from 1 second. 
    #We can always kill 1st monster.
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for d, s in zip(dist, speed):
            time.append(math.ceil(d/s))
        time.sort()
        print(time)
        for i in range(1,len(time)):
            if time[i] <= i:
                return i
        return len(time)
        
        