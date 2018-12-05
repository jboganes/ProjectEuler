#include <iostream>
#include <math.h> 
#include <map>
int divisorAmount(int n) {
    long int factors[10000];
    for (int x = 0; x < 10001; x++){
        factors[x] = 0;
    }
    int k = 0;
    
    while (n%2 == 0){ 
        factors[k] = 2;
        k++;
        n = n/2; 
    } 
    for (int i = 3; i <= sqrt(n); i = i+2) { 
        while (n%i == 0){ 
            factors[k] = i;
            k++;
            n = n/i; 
        } 
    }
    if (n > 2){
        factors[k] = n;
        k++;
    }
    
    std::map<int, int> bar;

    for (auto const &f : factors)
        bar[f]++;
   
    int divisors = 1;
    for (auto const &b : bar){
        if(b.first != 0){
            divisors *= (b.second + 1);
        }
    }
    return divisors;
} 
int main(){
    int num = 0;
    int k = 1;
    int divisors = 0;
    while (divisors < 501){
        num += k;
        k++;
        divisors = divisorAmount(num);
    }
    std::cout << num;
    return 0;
}
//Returns 76576500
