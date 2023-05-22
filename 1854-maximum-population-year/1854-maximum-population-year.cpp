class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        //since years are in range 1950 to 2050, we can 
        //create an array of size 100. each index stores count of population in that year
        int years[100]{0};

        //for each person
        for(int i=0;i<logs.size();i++){
            int startYears = logs[i][0];
            int endYears = logs[i][1];
            
            //increment population for all the years they were alive
            for(int j = startYears; j < endYears;j++){
                years[j-1950]++;
            }
        }
        
        //find the year with maximum population.
        int maxValue = INT_MIN;
        int maxIndex = 0;
        for(int i=0;i<100;i++){
            if(years[i] > maxValue){
                maxValue = years[i];
                maxIndex = i;
            }
        }
        return maxIndex+1950;
        
    }
};