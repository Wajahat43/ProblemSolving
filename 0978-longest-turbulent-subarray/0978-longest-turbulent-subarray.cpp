class Solution {
public:
    //It is like kadane's algorithm but we are not summing the values
    //instead we are keeping track of maximum size of subarray that satisfies the 
    //problem constraints.
    int maxTurbulenceSize(vector<int>& arr) {
        if (arr.size() == 1)
            return 1;
        int maxSize = 0;
        int currentSize = 1;

        //Case when arr[k] > arr[k + 1] when k is odd, and
        //arr[k] < arr[k + 1] when k is even. It might seem confusing but it is correct

        for (int i = 1; i < arr.size(); i++) {
            if (i % 2 == 0 && arr[i] < arr[i - 1])
                currentSize++;
            else if (i % 2 != 0 && arr[i] > arr[i - 1])
                currentSize++;
            else
                currentSize = 1;
            maxSize = max(currentSize, maxSize);
        }

        currentSize = 1;
        //Case when arr[k] > arr[k + 1] when k is even, and
        //arr[k] < arr[k + 1] when k is odd.
        for (int i = 1; i < arr.size(); i++) {
            if (i % 2 == 0 && arr[i] > arr[i - 1])
                currentSize++;
            else if (i % 2 != 0 && arr[i] < arr[i - 1])
                currentSize++;
            else
                currentSize = 1;

            maxSize = max(currentSize, maxSize);
        }

        return maxSize;
    }
};