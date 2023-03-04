class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int minIndex = -1, maxIndex = -1, subStartIndex = -1;
        long long subArrCount = 0;
        
        for(int i=0;i<nums.size();i++){
            
            if(nums[i] == minK)
                minIndex = i;
            
            if(nums[i] == maxK)
                maxIndex = i;
            
            if(nums[i] < minK || nums[i] > maxK)
                    subStartIndex = i;
            
            subArrCount += max(0, min(minIndex,maxIndex) - subStartIndex);
            
        }
        return subArrCount;
        
    }
};