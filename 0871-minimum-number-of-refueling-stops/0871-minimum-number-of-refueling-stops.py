from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [startFuel] + [0] * n
        #dp[i] is maximum distance we can reach by refueling at i stations
        for i in range(n):
            #for all the count of previous stations, check if we could reach current station
            for j in range(i, -1, -1):
                #if we could reach current station with j reufeling stops, update max distance of j+1 
                #to j+1's current value or dp[j] + currentStationsFuel.
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1], dp[j] + stations[i][1])
        for i in range(n+1):
            if dp[i] >= target:
                return i
        return -1
