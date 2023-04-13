class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        int pushedI = 0;
        int poppedI = 0;
        stack<int> st;
        for(int i=0;i<pushed.size();i++){
            st.push(pushed[i]);
            
                
            
            if(popped[poppedI] == pushed[i]){    
                while(st.empty() == false && poppedI < popped.size() && st.top() == popped[poppedI]){
                    st.pop();
                    poppedI++;
                }
            }
        }
        while(st.empty() == false){
            if(st.top() != popped[poppedI])
                return false;
            st.pop();
        }
        return true;
        
    }
};