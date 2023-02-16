class Solution {
public:
    int firstUniqChar(string s) {
        int chars[256]{0};
        for(int i=0;i<s.length();i++){
            chars[s[i]]++;
        }
        for(int i=0;i<s.length();i++){
            if(chars[s[i]] == 1){
                return i;
            }
        }
        return -1;
    }
};