class Solution {
public:
    //I noticed that on eah number we were coloring 4 additional boxes compared to last time
    long long coloredCells(int n) {
        if(n == 1)
            return 1;
        long long answer = 1;
        long long multiplyer = 4;
        for(int i=1;i<n;i++){
            answer += multiplyer;
            multiplyer += 4;
        }
        return answer;
        
    }
};