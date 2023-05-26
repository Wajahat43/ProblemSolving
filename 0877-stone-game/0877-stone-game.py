class Solution:
    
    def stoneGame(self, piles: List[int]) -> bool:
        visited = {}
        def game(piles, left, right, alicescore, bobscore, flag):
            if (left,right) in visited:
                return visited[(left,right)]
            if left < right:
                if flag:
                    res = game(piles, left+1,right,alicescore+piles[left],bobscore, not flag) or game(piles,left,right-1,alicescore+ piles[right],bobscore, not flag)
                else:
                    res = game(piles, left+1,right,alicescore,bobscore+piles[left],not flag) or game(piles,left,right-1,alicescore,bobscore+piles[right],not flag)
                visited[(left,right)] = res
                return res;
            return alicescore > bobscore;
        return game(piles,0,len(piles)-1,0,0,True)
                    
                    
        