class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = [-1 for i in range(len(nums2))]
        st = []
        elementIndex = {}

        #For each index i we will find the next greater element towards its right
        #stack will keep track of indexes whose next element we are yet to find
        #for those elements who don't have greater element towards their right, we have already
        #set the value to -1 when creating greater list
        for i in range(len(nums2)):
            while(len(st) > 0 and nums2[ st[-1] ] < nums2[i]):
                #nums2[i] is the next greater element of the element whose index is at top of stack
                greater[st[-1]] = nums2[i]
                #since we have found the next greater elemetn of the element with index at top of stack
                #we should pop it
                st.pop()
            #add the element with its index 
            elementIndex[nums2[i]] = i 
            #add it to stack (we need to find its greater element)
            st.append(i)
        res = []
        #for each element in num1
        for num in nums1:
            #find its index in num2
            index = elementIndex[num]
            #use greater array to answer the query of next greater towards right
            nextGreater = greater[index]
            #append it to our result
            res.append(nextGreater)
        return res

