#Trie
class Trie:
    #solution
    chars = 0
    #node
    def __init__(self):
        self.children = {}
        self.words = 0
        self.chars = 0
        self.isEnding = False
    #Modified insert
    def insert(self,s,i):
        #if we have inserted a word
        if i == -1:
            #if the word is not part of any longer word, we will insert it 
            #and make it part of our solution, otherwise ignore it.
            if len(self.children) == 0 and self.isEnding == False:
                self.isEnding = True
                Trie.chars += len(s)+1
            return 
                
        ch = s[i]
        #add child to dictionary
        if ch not in self.children:
            self.children[ch] = Trie()
        #if current word makes any previous word its prefix, then we will have to subtract this
        #prefix from our answer
        if self.isEnding == True:
            self.isEnding = False
            Trie.chars -= ((len(s)-i))
        #insert
        self.children[ch].insert(s,i-1)

class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        tr = Trie()
        Trie.chars = 0
        #insert each word in trie
        for word in words:
            tr.insert(word,len(word)-1)
            print(Trie.chars)
        #return solution
        return Trie.chars