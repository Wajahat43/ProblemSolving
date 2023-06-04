class Solution:
    #We will find the water trapped at each index
    #If there is a value greater than ith value towards left
    #and towards right that means our ith index will trap some water
    #it will trap the minimum of left or right height - val of ith index
    
    #We can create a postfix array to store maximum value towards right of each index
    #and for maximum value towards left, we just use a variable.
    def trap(self, height: List[int]) -> int:
        n = len(height)
        postfix = [-1]*n
        postfix[n-1] = height[n-1]

        total = 0
        for i in range(n-2,-1,-1):
            postfix[i] = max(height[i],postfix[i+1])

        leftMax = height[0]
        for i in range(1,n-1):
            if leftMax > height[i] and postfix[i+1] > height[i]:
                total += min(leftMax,postfix[i+1]) - height[i]
            
            leftMax = max(leftMax,height[i])
        return total