class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int characterCount [256]{0};
        
        for(int i=0;i<magazine.size();i++){
            char c = magazine[i];
            characterCount[c]++;
            cout << c << endl;
        }
        for(int i=0;i<ransomNote.size();i++){
            char c = ransomNote[i];
            characterCount[c]--;
            
            if(characterCount[c] < 0)
                return false;
            
            
        }
        return true;
        
        
        
    }
};