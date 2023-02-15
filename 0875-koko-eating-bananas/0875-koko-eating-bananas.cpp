class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        if(piles.size() == 0)
            return 0;

        long long int max = piles[0];
        //find the max element in array our answer cannot be greater than this max
        for(int i=0;i<piles.size();i++){
            if(piles[i] > max)
                max = piles[i];
        }
        
        //start from 1 to max and do binary search to find the lowest number that satisfies
        //the constraint.
        long long int low = 1;
        long int high = max;
        long long int solSoFar = INT_MAX;
        do{
            long long int mid = (high+low)/2;
            
            long long int timeTaken = 0;
            for(int i=0;i<piles.size();i++){
                timeTaken += ceil(piles[i]/(mid*1.0));
                if(timeTaken > h)
                    break;
            }
            if(timeTaken <= h && timeTaken < solSoFar){
                solSoFar = timeTaken;
            }
            if(timeTaken <= h){
                high = mid-1;
            }
            else{
                low = mid+1;
            }


        }while(low <= high);
        return low;
        
    }
};