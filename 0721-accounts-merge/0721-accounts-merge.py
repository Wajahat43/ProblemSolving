#declaring a union find structure
class UnionFind:
    def __init__(self,n):
        #parent of each node
        self.parents = [i for i in range(n)]
        #we can rank by height or size. Here we will rank by size
        self.rank = [1 for i in range(n)]
    
    #finds the root of a node 
    def find(self,curr):
        while curr != self.parents[curr]:
            #here we do path compression
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr
    #here we union (merge two disjoint sets)
    def union(self, first, second):
        fp = self.find(first)
        sp = self.find(second)
        
        #if sets are already unioned
        if fp == sp:
            return False
        #if first root has higher rank we will make it the parent
        if self.rank[fp] > self.rank[sp]:
            self.parents[sp] = fp
            self.rank[sp] += self.rank[fp]
        else:
            self.parents[fp] = sp
            self.rank[fp] += self.rank[sp]
        return True
            
        
            
            
    
        
class Solution:
    
    #instead of names we want to work with indexes (because names are not unique, indexes are)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #hash map to store index of owner of each account
        emailToAcc = {}
        uf = UnionFind(len(accounts))
        
        #we will do union of disjoint sets (merge accounts)
        for index, emails in enumerate(accounts):
            #skip first item in list because it is name of account
            for email in emails[1:]:
                #if we have not seen the email before
                if email not in emailToAcc:
                    emailToAcc[email] = index
                #if it is already in the map, that means we have two accounts with a similar email
                #implying they are same accounts
                else:
                    uf.union(index, emailToAcc[email])
        #Now we will store the emails of each accounts in a dictionary
        accToEmail = defaultdict(list)
        
        #since we have all the unique email in emialToAcc dictionary
        for email, index in emailToAcc.items():
            #we will find the leader through our union find data structure
            leader = uf.find(index)
            accToEmail[leader].append(email)
        
        res = []
        #Now that we have all the account indexes with the emails in each group we will cereate final result
        for index, emails in accToEmail.items():
            leaderName = accounts[index][0]
            
            #we will join two lists first list has name of leader and second has emails of that person
            res.append([leaderName] + sorted(accToEmail[index]))
            
        return res
            
        
                    