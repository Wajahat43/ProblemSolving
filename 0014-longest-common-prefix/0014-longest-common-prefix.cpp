class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int shortestLen = INT_MAX;
        //find the shortest string
        for(string str:strs){
            if(str.length() < shortestLen)
                shortestLen = str.length();
        }
        string result = "";
        for(int i=0;i<shortestLen;i++){
            //compare ith character of shortest string with ith character of all
            //other string, if the character doesn't match we have the solution.
            for(int j=0;j<strs.size()-1;j++){
                if(strs[j][i] != strs[j+1][i]){
                    return result;
                }
            }
            result += strs[0][i];
        }
        return result;
    }
};