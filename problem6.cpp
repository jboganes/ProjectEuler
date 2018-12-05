#include <iostream>
int main(){
    int sum, sqSum = 0;
    for (int i = 1; i < 101; i++){
        sqSum += i*i;
        sum += i;
    }
    std::cout << sum*sum - sqSum;
    return sum*sum - sqSum;
}
//Returns 25164150
