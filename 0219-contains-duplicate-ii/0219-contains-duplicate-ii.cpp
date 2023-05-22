class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;
        int left = 0;
        for(int i=0;i<nums.size();i++){
            if(i-left > k){
                window.erase(nums[left]);
                left++;
            }
            if(window.find(nums[i]) != window.end()){
                return true;
            }
            window.insert(nums[i]);
        }
        return false;
    }
};