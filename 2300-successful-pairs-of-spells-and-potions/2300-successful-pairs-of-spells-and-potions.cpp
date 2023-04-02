class Solution {
public:
    //The solution is simple, we must check each spell against all the potions.
    //but if we sort the potions in descending order and ith potion*spell > success
    //that implies that all previous potions than i will also will also be > sucess. As we sorted it in descending order.  
    //binary search
    int checkSpell(vector<int>& potions, int s, long long& success){
        int low = 0;
        int high = potions.size()-1;
        int ans = 0;
        while(low <= high){
            int mid = (low+high)/2;
            //to avoid integer overflow
            long long c = s;
            if(c*potions[mid] >= success){
                if(mid+1 >= ans)
                    ans = mid+1;
                low = mid+1;
            }
            else{
                high = mid-1;
            }
        }
        return ans;

    }
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        //sort the potions in descending order
        std::sort(potions.begin(),potions.end(),std::greater<int>());
        vector<int> rv;
        //for each spell get the answer using binary search
        for(int& s: spells){
            int result = checkSpell(potions, s, success);
            rv.push_back(result);
        }
        return rv;
    }
};