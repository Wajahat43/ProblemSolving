class Solution {
public:
    string removeStars(string s) {
        string result;
        int starsCount = 0;
        for(int i=s.length()-1;i>=0;i--){
            if(s[i] != '*' && starsCount == 0)
                result += s[i];
            else if(s[i] == '*')
                starsCount++;
            else
                starsCount--;
        }
        for(int i=0,j = result.length()-1;i<j;i++,j--){
            int temp = result[i];
            result[i] = result[j];
            result[j] = temp;
        }
        return result;
    }
};