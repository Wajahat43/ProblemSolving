class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def find_diff(word1, word2):
            diff = 0
            for c1, c2 in zip(word1,word2):
                if c1 != c2:
                    diff += 1
            return diff

        adjList = defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adjList[pattern].add(word)
        
        q = Deque()
        q.append(beginWord)
        visited = set()
        iteration = 1
        
        
        while q:
            
            for _ in range(len(q)):
                current_word = q.popleft()
                if current_word == endWord:
                    return iteration
                if current_word in visited:
                    continue
                visited.add(current_word)
                for j in range(len(current_word)):
                    pattern = current_word[:j] + "*" + current_word[j+1:]
                    for neiword in adjList[pattern]:
                        q.append(neiword)
                        
            iteration += 1
                
        return 0