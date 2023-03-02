class Solution {
public:
    int compress(vector<char>& chars) {
        //if empty vector return 0
        if (chars.size() == 0)
            return 0;
        char prev = chars[0];
        int currentIndex = 0;
        int count = 1;
        //iterate over the array
        for (int i = 1; i < chars.size(); i++) {
            //if current character is same as previous, increment it's count
            if (chars[i] == prev)
                count++;

            //if current character is different than prev, and it's count is only one, just add this character at curretnIndex and increment current Index
            else if (count == 1) {
                chars[currentIndex] = prev;
                prev = chars[i];
                currentIndex++;
            }
            else {
                
                //store prev character
                chars[currentIndex++] = prev;
                int idCount = 0;
                //store the count of prev character digit by digit
                while (count > 0) {
                    chars[currentIndex] = count%10 + '0';
                    currentIndex++;
                    count /= 10;
                    idCount++;
                }

                //as the count was stored in reverse order, reverse the count again.
                if(idCount > 1){
                    for (int k = currentIndex - idCount, j = currentIndex-1; k < j; k++, j--) {
                        char temp = chars[k];
                        chars[k] = chars[j];
                        chars[j] = temp;
                    }
              }

                prev = chars[i];
                count = 1;

            }
        }

        //Repeate for the last element
        if (count == 1) {
            chars[currentIndex++] = prev;
        }
        else {
            chars[currentIndex++] = prev;
            int idCount = 0;
            while (count > 0) {
                chars[currentIndex] = count%10 + '0';
                currentIndex++;
                count /= 10;
                idCount++;
            }
            if(idCount > 1){
                 for (int k = currentIndex - idCount, j = currentIndex-1; k < j; k++, j--) {
                char temp = chars[k];
                chars[k] = chars[j];
                chars[j] = temp;
            }
            }
           
        }
        return currentIndex;


    }
};