class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades = sorted(grades)
        groups = 1
        size = 1
        groupSum = grades[0]
        
        i = 1
        while i < len(grades):
            currentGroupSum = 0
            currentSize = 0
            
            
            j = i
            while j < len(grades):
                if currentGroupSum <= groupSum or currentSize <= size:
                    currentGroupSum += grades[i]
                    currentSize += 1
                    j+=1
                else:
                    break
            if groupSum < currentGroupSum and currentSize > size:
                groupSum = currentGroupSum
                size = currentSize
                groups += 1
            i = j
            
        return groups
                    
            
            