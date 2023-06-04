class UnionFind:
    def __init__(self,n):
        self.parents = {}
        self.rank = {}
        for i in range(n+1):
            self.parents[i] = i
            self.rank[i] = 0
        #at first all sets are disjoint. (no node is connected to each other)
        self.provinces = n
    
    def find(self, first):
        while first != self.parents[first]:
            #path compression
            self.parents[first] = self.parents[self.parents[first]]
            first = self.parents[first]
        return first

    def union(self, first,second):
        firstp = self.find(first)
        secondp = self.find(second)
        
        #if nodes are already part of same component
        if firstp == secondp:
            return False
        self.provinces -= 1

        if self.rank[firstp] < self.rank[secondp]:
            self.parents[firstp] = secondp
        elif self.rank[secondp] < self.rank[firstp]:
            self.parents[secondp] = firstp
        else:
            self.parents[firstp] = secondp
            self.rank[secondp] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        uf = UnionFind(rows)
        for i in range(rows):
            for j in range(cols):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i,j)
        return uf.provinces

        