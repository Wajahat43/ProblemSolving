class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        endTimes = []
        startTimes =[]
        result = [-1]*len(intervals)
        for i, interval in enumerate(intervals):
            endTimes.append((interval[1], i))
            startTimes.append((interval[0], i))
        heapq.heapify(endTimes)
        heapq.heapify(startTimes)

        while endTimes:
            end, i = heapq.heappop(endTimes)
            while startTimes and startTimes[0][0] < end:
                heapq.heappop(startTimes)
            if startTimes:
                result[i] = startTimes[0][1]
        return result


        