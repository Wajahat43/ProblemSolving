class Solution {
public:

    int lengthOfLongestSubstring(string s){
        unordered_set<char> substr;
        int L = 0;
        int maxSubstrSize = 0;
        for(int R = 0;R < s.length();R++){
            //until Rth character is in our substr, keep removing from left 
            //to avoid duplicates in substr
            while(substr.find(s[R]) != substr.end()){
                substr.erase(s[L]);
                L++;
            }

            substr.insert(s[R]);
            maxSubstrSize = max((int)maxSubstrSize, (int)substr.size());

        }
        return maxSubstrSize;
    }

   
   //my second attempt, uses sliding window but is slightly redudandant
    // int lengthOfLongestSubstring(string s) {
    //    unordered_set<char> charsInWindow;
    //    int L = 0;
    //    int longestSubStrSize = 0;
    //    for(int R = 0; R < s.length(); R++){
    //        if(charsInWindow.find(s[R]) == charsInWindow.end())
    //             charsInWindow.insert(s[R]);
    //         else{
    //             bool dupRemoved = false;
    //             do{
    //                 if(s[L] == s[R])
    //                     dupRemoved = true;
    //                 charsInWindow.erase(s[L]);
    //                 L++;

    //             }while(!dupRemoved);
    //             charsInWindow.insert(s[R]);
    //         }
    //         longestSubStrSize = max((int)charsInWindow.size(),longestSubStrSize);
           
    //    }
    //    return longestSubStrSize;
    // }
};