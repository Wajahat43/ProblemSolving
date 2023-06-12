class StockPrice:

    def __init__(self):
        #Two heaps to keep track of maximum and minimum values of stock
        self.maxHeap = []
        self.minHeap = []
        #Rates map to keep trac of newest rate at a given timestamp
        self.rates = {}
        #variable to keep track of most recent stock value
        self.curr = None
        
        

    def update(self, timestamp: int, price: int) -> None:
        #Insert the value to both heaps along with timestamp    
        heapq.heappush(self.minHeap,(price,timestamp))
        heapq.heappush(self.maxHeap,(price*-1,timestamp))
        #update the map
        self.rates[timestamp] = price
        #update the current value
        if self.curr == None or self.curr[0] <= timestamp:
            self.curr = (timestamp,price)
    
        

    def current(self) -> int:
        #return current value
        return self.curr[1]
        

    def maximum(self) -> int:
        #if heap top is correct return it
        if self.maxHeap[0][0] == self.rates[self.maxHeap[0][1]]:
            return self.maxHeap[0][0]*-1

        #pop the price and time from heap
        price,time = heapq.heappop(self.maxHeap)
        #until the price doens't match the updated price of stock from map for the given time stamp, that means it was updated and should removed from heap
        while price != self.rates[time]*-1:
            price,time = heapq.heappop(self.maxHeap)
        
        #add the last valid value back to heap
        heapq.heappush(self.maxHeap,(price,time))
        #return the price
        return price*-1
        

    def minimum(self) -> int:
        #same as above except with minHeap
        if self.minHeap[0][0] == self.rates[self.minHeap[0][1]]:
            return self.minHeap[0][0]

        price,time = heapq.heappop(self.minHeap)
        while price != self.rates[time]:
            price,time = heapq.heappop(self.minHeap)
        
        heapq.heappush(self.minHeap,(price,time))
        return price
        
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()