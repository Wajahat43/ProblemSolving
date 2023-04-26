class Solution {
public:
     int add(int num){
        int sum =0;
        while(num > 0)
        {
            sum += num%10;
            num /= 10;
        }
         return sum;
    }
    
    int addDigits(int num) {
        int res = add(num);
        while(res > 9)
            res = add(res);
        return res;
        
    }
};