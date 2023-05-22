class Solution {
public:
    
    //This function check if for given window size k
    //if there a subarray with sum >= target
    bool hasSum(vector<int>& nums, int target, int k){
        int sum = 0;
        for(int i = 0; i < nums.size()+1;i++){
            //if i is in range of nums
            if(i < nums.size())
                sum += nums[i];
            
            //if i is greater than window size
            //subtract left most element from sum
            if(i >= k){
                sum -= nums[i-k];
            }
            
            //if we have reached target return true
            if(sum >= target)
                return true;
        }
        return false;
    }
    //we observe that minimum window size can be 1 and maximum window size
    //can be size of nums. Therefore, I use binary search to check if
    //a window size of mid can form sum. If it can then all window size greater than it can also 
    //and if it can't then all window size less than it also can't
    int minSubArrayLen(int target, vector<int>& nums) {
        int min = 1;
        int max = nums.size();
        int ans = INT_MAX;
        //binary search
        while(min <= max){
            int mid = (min+max)/2;
        
            if(hasSum(nums,target,mid)){
                max = mid-1;
                ans = mid;
            }
            else
                min = mid+1;
        }
        if(ans == INT_MAX)
            return 0;
        return ans;
        
    }
};