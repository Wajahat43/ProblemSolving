class Trie {
    
    struct Node{
        Node* children [26];
        bool isLeaf;
        
        Node(){
            for(int i=0;i<26;i++){
                children[i] = nullptr;
            }
            isLeaf = false;
        }
        
    };
    
    Node root;
public:
    Trie() {
        
    }
    
    void insert(string word) {
        Node* current = &root;
        for(int i=0;i<word.length();i++){
            int index = word[i] - 'a';
            if(current->children[index] == nullptr){
                current->children[index] = new Node();
            }
            if(i == word.size()-1){
                current->children[index]->isLeaf = true;
            }
            current = current->children[index];
        }
        
    }
    
    bool search(string word) {
        Node* current = &root;
        for(int i=0;i<word.length();i++){
            int index=word[i] - 'a';
            if(current->children[index] == nullptr)
                return false;
            if(i == word.length()-1 && current->children[index] && current->children[index]->isLeaf)
                return true;
            current = current->children[index];
        }
        return false;
        
    }
    
    bool startsWith(string prefix) {
        Node* current = &root;
         for(int i=0;i<prefix.length();i++){
            int index=prefix[i] - 'a';
            if(current->children[index] == nullptr)
                return false;
             current = current->children[index];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */