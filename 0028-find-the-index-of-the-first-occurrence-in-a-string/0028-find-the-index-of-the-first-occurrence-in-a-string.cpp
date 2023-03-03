class Solution {
public:
    int strStr(string haystack, string needle) {
        int needleIndex = 0;
        for(int i=0;i<haystack.length();i++){
            if(haystack[i] == needle[needleIndex]){
                needleIndex++;
            }
            else{
                i -= needleIndex;
                needleIndex = 0;
                
            }
            if(needleIndex == needle.length()){
                return i - (needle.length()-1);
            }

        }
        return -1;
      
        
    }
};