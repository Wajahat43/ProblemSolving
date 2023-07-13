class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(i,j,ind):
            if board[i][j] != word[ind]:
                return False
                
            if ind >= len(word)-1:
                    return True
          

            visited.add((i,j))
            moves = [(1,0),(0,1),(0,-1),(-1,0)]

            for move in moves:
                nexti = i + move[0]
                nextj = j + move[1]

                if nexti >= 0 and nexti < rows and nextj >= 0 and nextj < cols and board[nexti][nextj] == word[ind+1] and (nexti,nextj) not in visited:
                    if dfs(nexti,nextj,ind+1) == True:
                        return True
            visited.remove((i,j))
            return False
                        
                    
        
        for i in range(rows):
            for j in range(cols):
                visited.clear()
                if dfs(i,j,0) == True:
                    return True
        return False
                    



