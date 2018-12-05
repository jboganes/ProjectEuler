#include <iostream>
int findNextFibonacci(int f, int fPrev){
    return (f + fPrev);
}
int main(){
    int f = 2;
    int fPrev = 1;
    int fTemp, sum = 0;
    while (f <= 4000000){
        if ((f%2)==0){
            sum += f;
        }
        fTemp = f;
        f = findNextFibonacci(f, fPrev);
        fPrev = fTemp;
    }
    return sum;
}
//Returns 4613732 
