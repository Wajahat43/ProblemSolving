class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        val = {}
        for i,c in enumerate(order):
            val[c] = i


        def inOrder(first,second):
            #index of first string
            i = 0
            #index of second string
            j = 0
            while i < len(first) and j < len(second):
                #character at ith index of each string
                c1 = first[i]
                c2 = second[j]
                #if the value of c1 is less than value of c2, that means strings are in order
                if val[c1] < val[c2]:
                    return True
                #if it is greater then the strings are in wrong order
                elif val[c1] > val[c2]:
                    return False
                i += 1
                j += 1
            
            if i == len(first):
                return True
            else:
                return False
        
        for i in range(len(words)-1):
            current = words[i]
            nextWord = words[i+1]
            if inOrder(current,nextWord) == False:
                return False
        return True
            