class Solution:
    #The trick is that the first number in list will be adjacent to only one other number and hence it will occur only once in ajdacent pairs. 
    #Then for each subsequent number,  you can just find what was its pair
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mappings = defaultdict(list)
        freq = defaultdict(int)
        for first,second in adjacentPairs:
            mappings[first].append(second)
            mappings[second].append(first) 
            freq[first] += 1
            freq[second] += 1
        unique = float("infinity")
        for key, value in freq.items():
            if value == 1:
                unique = key
        
        result = []
        current = unique
        used = set()

        while len(result) <= len(adjacentPairs):
            result.append(current)
            used.add(current)
            next = mappings[current][0] if mappings[current][0] not in used or len(mappings[current]) == 1 else mappings[current][1]
            current = next
        return result
            
        

            
        