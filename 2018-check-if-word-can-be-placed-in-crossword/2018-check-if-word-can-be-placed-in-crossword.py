class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def placeUp(row,col,i):
            #if we have reached end of word and ended in a valid position
            if i == len(word) and (row < 0 or board[row][col] == '#'):
                return True
            #if we have reached end of word or are out of boudns of matrix
            elif i == len(word) or row < 0:
                return False

            #if we can place ith character at the current box
            if board[row][col] == word[i] or board[row][col] == ' ':
                return placeUp(row-1,col,i+1)
            else:
                return False
        def placeDown(row,col,i):
            if i == len(word) and (row >= rows or board[row][col] == '#'):
                return True
            elif i == len(word) or row >= rows:
                return False
            if board[row][col] == word[i] or board[row][col] == ' ':
                return placeDown(row+1,col,i+1)
            else:
                return False
        def placeLeft(row,col,i):
            if i == len(word) and (col < 0 or board[row][col] == '#'):
                return True
            elif i == len(word) or col < 0:
                return False
            if board[row][col] == word[i] or board[row][col] == ' ':
                return placeLeft(row,col-1,i+1)
            else:
                return False
        def placeRight(row,col,i):
            if i == len(word) and (col >= cols or board[row][col] == '#'):
                return True
            elif i == len(word) or col >= cols:
                return False
            if board[row][col] == word[i] or board[row][col] == ' ':
                return placeRight(row,col+1,i+1)
            else:
                return False
        
        for i in range(rows):
            for j in range(cols):
                #first we check if we can start at that specific box and then try all the 4 combinations.
                if i+1 >= len(word)and (i+1 >= rows or board[i+1][j] == '#') and placeUp(i,j,0) :
                    return True
                if rows - i+1 >= len(word) and (i-1 < 0 or board[i-1][j] == '#')and placeDown(i,j,0) :
                    return True
                if j+1 >= len(word)and (j+1 >= cols or board[i][j+1] == '#') and placeLeft(i,j,0) :
                    return True
                if cols - j+1 >= len(word)and  (j-1 < 0 or board[i][j-1] == '#') and placeRight(i,j,0) :
                    return True
        return False

        
        
