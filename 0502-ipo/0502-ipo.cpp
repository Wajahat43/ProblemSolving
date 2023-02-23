class Solution {
    //custom structure
    struct Record{
        int profit;
        int capital;
        
        //overloaded methods to be used for creating minheap
        bool operator > (const Record& left) const{
            return this->capital > left.capital;
        }
        bool operator >= (const Record& left) const{
            return this->capital >= left.capital;
        }
    };
public:

    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        //create a min heap
        std::priority_queue<Record,std::vector<Record>,greater<Record>> minHeap;
        //create a max heap of profits
        std::priority_queue<int> maxHeap;

        //insert all data into the min heap
        for(int i=0;i<profits.size();i++){
            Record record;
            record.profit = profits[i];
            record.capital= capital[i];
            minHeap.push(record);
        }

        while(k > 0){
            //until heap is not empty and top of heap project can be undertaken
            //add it to the max heap (that has projects that can be started)
            while(!minHeap.empty() && minHeap.top().capital <= w){
                maxHeap.push(minHeap.top().profit);
                minHeap.pop();
            }
            //if there are no more projects that can be started, return answer so far
            if(maxHeap.empty())
                return w;
            //from the projects that can be started choose the one with max profit
            w += maxHeap.top();
            maxHeap.pop();
            k--;
        }

        return w;
       
      
        

    }
    //This solution is ineffecient
    // void recursive(vector<Record>& records, int current, int k, int w, int& answer){
    //     if(w > answer)
    //         answer = w;
    //     if(k == 0 || current >= records.size() || records[current].capital > w)
    //         return;
        
    //     recursive(records,current+1,k-1,w + records[current].profit,answer);
    //     recursive(records,current+1,k,w,answer);

    // }
    // int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
    //     vector<Record> records;
    //     for(int i=0;i<profits.size();i++){
    //         Record record;
    //         record.profit = profits[i];
    //         record.capital= capital[i];
    //         records.push_back(record);
    //     }
    //     std::sort(records.begin(),records.end(),[](const Record& first, const Record& second){
    //         if(first.capital == second.capital){
    //             return first.profit > second.profit;
    //         }
    //         return first.capital < second.capital;
    //     });

    //     int answer = INT_MIN;
    //     recursive(records,0,k,w,answer);
    //     return answer;

    // }
};