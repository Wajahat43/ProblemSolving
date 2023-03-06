class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int arrIndex = 0;
        int missingCount = 0;
        int current = 1;
        while(missingCount < k){
            if(arrIndex < arr.size() && arr[arrIndex] == current){
                arrIndex++;
            }
            else{
                missingCount++;
            }
            if(missingCount == k)
                return current;
            current++;
        }
        return current;
        
        
    }
};