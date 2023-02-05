#include<iostream>
using namespace std;


int main(){


    int a, b;
    int A = 3124;
    int B = 5162;
    int x = 10;

    while(A > 0){

        a = A%10;
        b = B%10;
        if((x-a)  == b){

            cout << "possible";
            
        }
    }
}