class Solution {
public:
    
    //we want to split the number into two numbers such that they form
    //minimum numbers
    int splitNum(int num) {
        //create a vector of digits of number
        vector<int> digits;
        while(num > 0){
            digits.push_back(num%10);
            num/=10;
            
        }
        //sort the digits in descending order
        std::sort(digits.begin(),digits.end());
        int num1 = 0;
        int num2 = 0;
        bool first = true;
        
        //for each digit append it to first or second 
        //doing this becaue if we want to create two minimum numbers we must
        //assign the smallest digits to msb of each number alternatively.
        for(int i=0;i<digits.size();i++){
            if(first){
                num1 = num1*10 + digits[i];
            }
            else{
                num2 = num2*10 + digits[i];
            }
            first = !first;
        }
        //return the sum of two numbers
        return num1 + num2;
        
        
    }
};