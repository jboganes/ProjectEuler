#include <iostream>
#include <cstring> 
#include <algorithm>
bool isPalindrome(int num){
    std::string str = std::to_string(num);
    std::string revStr = str;
    std::reverse(revStr.begin(), revStr.end());
    return !str.compare(revStr);
}
int main(){
    int product;
    int maxPal = 0;
    for (int i = 1000; i > 99; i--){
        for (int j = 1000; j > 99; j--){
            product = i*j;
            if (isPalindrome(product) && product>=maxPal){
                maxPal = product;
            }
        }
    }
    std::cout << maxPal;
    return 0;
}
//Returns 906609
