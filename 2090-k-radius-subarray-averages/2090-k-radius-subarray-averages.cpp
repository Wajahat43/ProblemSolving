class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        //these two vectors will store prefix and postfix sums
        //at in index i with a maxium window size of k
        vector<long long> prefix(nums.size(),0);
        vector<long long> postfix(nums.size(),0);
        //intially set all the values in resulting vector to -1
        vector<int> result(nums.size(),-1);

        //calculating prefix sum of the vector
        long long localSum = 0;
        for(int i=0;i<nums.size();i++){
            prefix[i] = localSum;
            localSum += nums[i];
            if(i >= k){
                localSum -= nums[i-k];
            }
        }

        //calculating postfix sum of the vector
        localSum = 0;
        for(int i=nums.size()-1;i>=0;i--){
            postfix[i] = localSum;
            
            localSum += nums[i];
            if(nums.size()-i > k){
                localSum -= nums[i+k];
            }
        }

        //start with indices which has atleast k elements before them and
        //end at indices which has atleast k elements after them
        //find the average using the k-window sized prefix and postfix sum.
        for (int i = k; (i < nums.size() - k) && i < nums.size(); i++){
            result[i] = (prefix[i] + postfix[i]+nums[i]) / (k*2+1);
        }
        
        return result;
        
    }
};