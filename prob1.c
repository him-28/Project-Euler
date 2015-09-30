#include<stdio.h>
#include<stdlib.h>
int main()
{
    int sum = 0;
    int i;
 
 
    for (i=0; i < 1000; i++)
    {
        if (i % 3 == 0 || i % 5 == 0){
	 printf(" \n\n%d\n\n",i);
        sum += i;}
         
 
        
    }
 
    printf(" \n\n%d\n\n",sum);
 
    return 0;
}
