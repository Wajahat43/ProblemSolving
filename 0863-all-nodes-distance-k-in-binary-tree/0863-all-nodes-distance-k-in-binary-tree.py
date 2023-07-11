# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        adjList = collections.defaultdict(list)

        def createList(current):
            if (current == None):
                return

            if current.left:
                adjList[current.val].append(current.left.val)
                adjList[current.left.val].append(current.val)
            if current.right:
                adjList[current.val].append(current.right.val)
                adjList[current.right.val].append(current.val)

            createList(current.left)
            createList(current.right)
        createList(root)

        
        res = []
        def dfs(current, k,parent):
            if k  == 0:
                res.append(current)  
                return

            for node in adjList[current]:
                if node != parent:
                    dfs(node,k-1,current)

        dfs(target.val, k, None)
        return res
