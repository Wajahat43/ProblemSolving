class Solution:
    #this seems like a class BFS problem. BFS gurantees to find the minimum distance in unweighted grah
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        #moves we can make
        moves = [(1,0),(0,1),(0,-1),(-1,0)]
        visited = set()
        q = deque()
        #append the current postion to queue and its distance 0
        q.append(entrance + [0])

        while len(q) > 0:
            #pop current position
            pos = q.popleft()

            #if we have reached an edge cell that is nto starting cell, return distacne
            if (pos[0] == 0 or pos[0] == rows-1 or pos[1] == 0 or pos[1] == cols-1) and (pos[0] != entrance[0] or pos[1] != entrance[1]):
                return pos[2]
            #create tuple of position, to store in set
            pp = (pos[0],pos[1])
            if pp not in visited:
                #try to move in all four directions
                for move in moves:
                    #get neighbouring coordinates
                    x = pos[0] + move[0]
                    y = pos[1] + move[1]

                    #if they are valid and cell is also empty, add to queue to visite
                    if x >= 0 and x < rows and y >= 0 and y < cols and maze[x][y] == '.':
                        q.append([x,y, pos[2]+1])
                #add the tupe of current position to visited.
                visited.add(pp)
        
        return -1

                


                



