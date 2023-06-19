class Solution:
    #The approach is to basically, iterate over the each word in words array
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        startsWith = defaultdict(list)
        count = 0
        for word in words:
            startsWith[word[0]].append(word)
        
        for currentChar in s:
            allPossible = startsWith[currentChar]
            startsWith[currentChar] = list()

            for word in allPossible:
                if len(word) == 1:
                    count += 1
                else:
                    startsWith[word[1]].append(word[1:])

        return count
        