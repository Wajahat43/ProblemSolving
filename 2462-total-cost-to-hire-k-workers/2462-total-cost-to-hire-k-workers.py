class Solution:
    #We need to choose the lowest cost workers from either
    #the start n candidates or from last n candidates. Lowest from a list is minheap
    #This is two heaps problem
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lowWorkers = []
        highWorkers = []
        lowIndex = 0
        highIndex = len(costs)-1
        

        #Insert the first n candidates to their heap
        while lowIndex < len(costs) and lowIndex < candidates:
            heapq.heappush(lowWorkers, costs[lowIndex])
            lowIndex += 1
        
        #Insert the last n candidates to their heap
        while highIndex >= 0 and len(costs)-highIndex <= candidates and highIndex >= lowIndex:
            heapq.heappush(highWorkers,costs[highIndex])
            highIndex -= 1

        #Variables to keep track of cost so far and number of selected candidates
        cost = 0
        selected = 0

        while selected < k:
            #if we want to take the worker from first half
            if (lowWorkers and highWorkers and lowWorkers[0] <= highWorkers[0]) or len(highWorkers) == 0:
                x = heapq.heappop(lowWorkers)
                (x)
                cost += x
                #if there are more workers, insert them to first half (since we just created space by taking a worker from here)
                if lowIndex <= highIndex:
                    heapq.heappush(lowWorkers, costs[lowIndex])
                    lowIndex += 1
            #if we need to take worker from last half
            else:
                x = heapq.heappop(highWorkers)
                cost += x
                
                if highIndex >= lowIndex:
                    heapq.heappush(highWorkers, costs[highIndex])
                    highIndex -= 1
            selected += 1
        
        return cost

                    

        

        