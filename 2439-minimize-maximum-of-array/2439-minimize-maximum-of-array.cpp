class Solution {
public:
    //1st number cannot be decreased to our answer cannot be less than it.
    //at ith index we can evenly distribute sum of values until index i 
    //for example 1,3,9 can be 4,4,5
    //so we maintain a prefix sum and to evenly distribute we take sum/count of value (i+1)
    
    int minimizeArrayValue(vector<int>& nums) {
        
        int result = nums[0];
        long long sumSoFar = nums[0];
        
        for(int i=1;i<nums.size();i++){
            sumSoFar += nums[i];
            int localResult = ceil(sumSoFar/(i+1.0));
            if(localResult > result)
                result = localResult;
        }
        return result;
      

    }
};