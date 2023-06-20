import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity

        #We will use pushHeap as minHeap because we want to pop from left with the lowest index
        self.pushHeap = [0]
        #We will use popHeap as maxHeap (because we want to pop from right with the highest index)
        self.popHeap = []
        self.data = [[]]
        
        

    def push(self, val: int) -> None:
        index = 0
        while self.pushHeap:
            index = heapq.heappop(self.pushHeap)
            if len(self.data[index]) != self.cap:
                break

        #if pushHeap is empty, append an empty list to our self.data
        if len(self.data[index]) == self.cap:
            index = len(self.data)
            #append an empty list to our self.data
            self.data.append([])

        self.data[index].append(val)
        if len(self.data[index]) != self.cap:
            #insert to push heap to represent that this index can store new values
            heapq.heappush(self.pushHeap,index)
        #insert index to pop heap, so that we know this index has a vlaue that can be popped. 
        heapq.heappush(self.popHeap,index*-1)
        
            

        
        

    def pop(self) -> int:
        #until pop heap is not empty
        while self.popHeap:
            #Get the highest index
            index = heapq.heappop(self.popHeap)*-1
            #if the highest index has some value, pop value from it
            #otherwise try next highest index
            if len(self.data[index]) != 0:
                return self.popAtStack(index)
        #if pop heap is empty, return -1
        return -1


        

    def popAtStack(self, index: int) -> int:
        #if index is out of range or stack at that index is empty
        if index > len(self.data) or len(self.data[index]) == 0:
            return -1
        

        #Access the last element
        val = self.data[index][-1]
        #pop the last element
        self.data[index].pop()

                #push the index to pushHeap since now it will have space for 1 element that wejust popped
        heapq.heappush(self.pushHeap,index)
        #return the value at last element
        return val