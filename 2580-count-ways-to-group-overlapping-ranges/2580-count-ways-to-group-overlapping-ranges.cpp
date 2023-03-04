class Solution {
public:
    //The approach is to count unique intervals. And the answer will be 2^unique_intervals
    //because we want to choose 2 values out of those n unique_intervals and want to find the total number of ways
    int countWays(vector<vector<int>>& ranges) {    
        //count of unique intervals
        int counter = 1;
        //sort the ranges based on their start value
        std::sort(ranges.begin(),ranges.end());
        //take the first range as start
        pair<int,int> current = {ranges[0][0],ranges[0][1]};
        
        //for all the ranges
        for(int i = 1;i<ranges.size();i++){
            //if the end of current range is greater than or equal to start of next range
            //that means that they should be merged and update end of current range
            if(current.second >= ranges[i][0]){
                current.second = max(current.second,ranges[i][1]);
            }
            //otherwise update current range and increase count of current range
            else{
                counter++;
                current.first = ranges[i][0];
                current.second = ranges[i][1];
            }
        }
        
        //Calculate the power
        long long answer = 1;
        for(int i = counter;i>=1;i--){
            answer = ((long long)2* answer) % (1000000007);
        }
        return answer;;
        
        
    }
};