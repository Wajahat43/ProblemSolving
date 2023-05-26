class Solution:
    #Idea is to use memorization and recursion. IT took me 46 mins to solve.
    #at each turn we can have two recursive calls one with left++ or one with right--
    #so that is done and we also have a visited dictionary to not do recursive calls
    #on left and right we have already checked because the result will be same. This 
    #saves a lot of overlapping recursive calls 
    def stoneGame(self, piles: List[int]) -> bool:
        visited = {}
        #helper method
        def game(piles, left, right, alicescore, bobscore, flag):
            #if we have already visited this (left,right) pair
            if (left,right) in visited:
                return visited[(left,right)]
            #if the list has values left
            if left < right:
                #if it is alice's turn add the score to alic
                if flag:
                    res = game(piles, left+1,right,alicescore+piles[left],bobscore, not flag) or game(piles,left,right-1,alicescore+ piles[right],bobscore, not flag)
                #if it is bob's turn add the score to bob
                else:
                    res = game(piles, left+1,right,alicescore,bobscore+piles[left],not flag) or game(piles,left,right-1,alicescore,bobscore+piles[right],not flag)
                #store the result in dictionary and return it
                visited[(left,right)] = res
                return res;
            #if we have reached end of array, return if alice has more score than bob
            return alicescore > bobscore;
        return game(piles,0,len(piles)-1,0,0,True)
                    
                    
        