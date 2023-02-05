#include <bits/stdc++.h>
#include<fstream>
using namespace std;
int main() {
   int max;
   max = 1000; //set the upper bound to generate the random number
   srand(time(0));
   ofstream fout;
	fout.open("meso.txt");
	int flag=0;
   for(int i=0;i<100;i++)
   {
   		if(flag==0)
   		{
//   			fout<<rand()%max;
   			fout<<((double)rand()/(RAND_MAX)); //only for bucket sort
   			flag=1;
		}
		else{
			fout<<" ";
//			fout<<rand()%max;
			fout<<((double)rand()/(RAND_MAX));	 //only for bucket sort
		}
		
   }
   fout.close();
}
