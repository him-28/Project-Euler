#include <stdio.h>
#include <stdlib.h>
//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
int main()
{
   int sum1=0,sum2=0,psum=0,i=0;

   for( i=1;i<=100;i++)
   sum1+=i*i;

   for( i=1;i<=100;i++)
   psum+=i;
   sum2=psum*psum;

   printf("\nDifference is: %d\n",sum2-sum1);


}
