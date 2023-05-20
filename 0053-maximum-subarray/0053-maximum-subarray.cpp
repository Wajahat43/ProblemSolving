class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        //create two variables to hold current and max sum
        int currentSum =0;
        int maxSum = nums[0];

        //iterate over the array
        for(int n:nums){
            //if at any point the current sum becomes negative, we want to ignore it 
            //for the next values. Because adding negative will cause our sum to decrase.
            //here we don't skip negative numbers because a negative number might have another positive
            //number after it that might bebigger than it.
            if(currentSum < 0)
                currentSum = 0;
            //add current element to the sum
            currentSum += n;

            //choose the max sum
            maxSum = max(maxSum,currentSum);
        }
        //return maxSum
        return maxSum;
        
    }
};