class Solution {
public:
    bool isPalindrome(int x) {
        int a = x;
        //int l= 0;
        long long l = 0;

        while (a>0){
        
            l = a%10 + 10*l;
            a = a/10;
        }

        if (x == l){
            return true;
        } else{
            return false;
        } 
        
    }
};