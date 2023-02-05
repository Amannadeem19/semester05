#include<iostream>
using namespace std;


int main(){


    int array[6] = {10, -10, 20, 30, -20, 60};

    int sum[6] = 0;
    int i = 0;
    int j = 0;
    while (i < 6)
    {
        
    
    if(array[i] < 0){

        i++;
        j++;

    }
    else if(array[i] > 0){

        sum[j] += array[i];
        i++;
    }


    }

    while (i < sum.length())
    {
        /* code */
    }
    
    
    
}