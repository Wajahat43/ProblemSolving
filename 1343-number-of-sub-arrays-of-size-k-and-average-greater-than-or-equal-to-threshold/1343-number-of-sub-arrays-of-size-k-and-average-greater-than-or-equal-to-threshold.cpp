class Solution {
public:
    //we will use fixed size sliding window
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        //sum
        long long sum = 0;
        //our left pointer of window
        int l = 0;
        //count of solution
        int count = 0;

        //iterate over the array and for r == arr.size()
        for (int r = 0; r < arr.size()+1; r++) {
            //if size of our window is greater than k subtract the left most element from window
            //and move left to next
            if (r - l > k) {
                sum -= arr[l];
                l++;
            }

            //if size of window is k and average >= threhold increment count
            if (r - l == k && (sum / (double)k) >= threshold)
                count++;
            //if right is in bounds of array add value at r to sum
            if(r < arr.size())
                sum += arr[r];

        }

        return count;

    }
};