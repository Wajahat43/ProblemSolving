class RandomizedSet:

    def __init__(self):
        self.data = []
        self.mappings = {}

    def insert(self, val: int) -> bool:
        if val in self.mappings:
            return False
        self.data.append(val)
        self.mappings[val] = len(self.data)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.mappings:
            return False
        mapping = self.mappings[val]
        last_val = self.data[-1]
        self.data[mapping], self.data[-1] = self.data[-1], self.data[mapping]
        self.data.pop()
        self.mappings[last_val] = mapping
        del self.mappings[val]
        return True

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.data)-1)
        return self.data[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()