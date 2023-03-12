class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int first[256]= {0},second[256]={0};
        for(int i=0;i<s.length();i++){
            first[s[i]]++;
            second[t[i]]++;
            if(first[s[i]] != second[t[i]])
                return false;
            first[s[i]] = second[t[i]] = i+1;
        }
        
        int uF = 0, uS = 0;
        for(int i=0;i<256;i++){
            if(first[i] != 0)
                uF++;
            if(second[i] != 0)
                uS++;
        }
        return uF == uS;
    }
};