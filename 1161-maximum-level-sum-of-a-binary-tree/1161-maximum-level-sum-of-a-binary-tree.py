class Solution:
    #This is a class BFS problem, except we need to store level of each node as well.
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()

        q.append((root,1))
        currentLevel = 1
        levelSum = root.val
        maxSum= root.val
        minLevel = 1
        #utnil q is not empty
        while q:
            #pop current node and its level
            current,level = q.popleft()

            #if elvel is 1 or level is not equal to current level, that means we are moving to next level
            if level != currentLevel or level == 1:
                #before moving to next level update the answer
                if levelSum > maxSum:
                    maxSum = levelSum
                    minLevel = currentLevel

                #reset the currentLevel and levelSum
                levelSum = current.val
                currentLevel = level
            else:
                levelSum += current.val

            #add children to queue if they are not emtpy
            if current.left != None:
                q.append((current.left, level+1))
            if current.right != None:
                q.append((current.right, level+1))
        
        # Compare the last level's sum to maxSum
        if levelSum > maxSum:
            maxSum = levelSum
            minLevel = currentLevel
        #return the minLevel
        return minLevel
