class Solution:
    #This is a standard graph problem
    #Question states that graph is bipartite such that every edge in the graph connects a node in Set A and a node in set B. That means that nodes on both sides of edges must be from different sets. We use color to represent the set to which they belong. 

    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        nodes = len(graph)
        #intially all nodes have color white (they don't belong to any set)
        for i in range(nodes):
            colors[i] = 'white'
        visited = set()

        #performs dfs on the graph
        def dfs(current, color):
            #get neighbours
            neighbours = graph[current]
            #set color and also add to visited set
            colors[current] = color
            visited.add(current)
            #for each neighbour
            for ne in neighbours:
                #if color of neighbour is same as color of current node, that means that both nodes of an edge belong to same gropu so return False
                if colors[ne] != 'white' and colors[ne] == color:
                    return False
                #dfs on neighbor if it is not already visited.
                if ne not in visited:
                    if dfs(ne,'red' if color == 'green' else 'green') == False:
                        return False
            
            return True

        #as the graph is disconnected, we visit every node that is not visited one by one
        for node in range(nodes):
            if node not in visited:
                if dfs(node,"red") == False:
                    return False
        return True
                    
                
                
                
                