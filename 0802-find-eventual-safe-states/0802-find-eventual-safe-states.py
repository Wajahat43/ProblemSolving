class Solution:
    #Observations
    #1. If I reach a node with no outgoing edges that means this path ended in a terminal node
    #2. For a node to be safe, all it's paths should be terminal.
    #3. So we have to check all the neighbors before declaring a node safe
    #4. Seems similar to topological sorting or dfs
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()
        safe = set()

        def isSafe(current):
            if current in visited:
                if current in safe:
                    return True
                return False
        
            #mark current as visited
            visited.add(current)
            
            #check if all its neighbors are safe
            for node in graph[current]:
                #if any of its neighbors is not safe, this node is not safe
                if isSafe(node) == False:
                    return False

            #if all neighbors are safe,then this is safe
            safe.add(current)
            return True
        
        #check every node to see if it is safe
        for i in range(len(graph)):
            isSafe(i)
    
        return sorted(list(safe))
        


            



            
