#include <iostream>
long nextNum(long n);
long getChainLength(long n);
int main(){
    long len = 0;
    long maxLen = 0;
    long maxLenNum = 0;
    for (long i = 1000000; i > 0; i--){
        len = getChainLength(i);
        if (len >= maxLen){
            maxLen =  len;
            maxLenNum = i;
        }
    }
    return maxLenNum;
}
long nextNum(long n){
    if(n%2 == 0){
        return (n/2);
    }else{
        return (3*n + 1);
    }
}
long getChainLength(long n){
    long len = 0;
    while (n!=1){
        n = nextNum(n);
        len++;
    }
    return len+1;
}
//Returns 837799
