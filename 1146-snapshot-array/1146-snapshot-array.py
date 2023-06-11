class SnapshotArray:
    #Essentially at each index we store the value along with its snap id
    #and then when we want a value at specific index with specific snap id
    #we do binary search on snap id to find the value
    def __init__(self, length: int):
        self.data = [[] for i in range(length)]
        for i in range(length):
            self.data[i].append([0,0])
        self.snapId = 0
        

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][1] == self.snapId:
            self.data[index][-1] = [val,self.snapId]
        else:
            self.data[index].append([val,self.snapId])

        
        

    def snap(self) -> int:
        self.snapId+= 1
        return self.snapId-1
        
        
    def get(self, index: int, snap_id: int) -> int:
        records = self.data[index]

        low = 0
        high = self.snapId
        closest = 0
        while low <= high:
            mid = low + (high-low)//2

            if mid < len(records) and records[mid][1] == snap_id:
                return records[mid][0]
            elif mid < len(records) and records[mid][1] < snap_id:
                closest = records[mid][0]
                low = mid+1
            else:
                high = mid-1
        return closest
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)