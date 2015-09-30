#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<stdbool.h>
int main(){
        int counter = 1;
        bool prime = 1;
        double numerator = 0;
        double denominator = 0;
        double denom = 0.0;

        do {
            numerator++;
            denom = numerator / 2;
            denominator = ceil(denom);
            prime = 1;

            for (int i = 2; i <= (int)denominator + 1; i++){
                if((int)numerator % i == 0){
                    prime = 0;
                }
            }
            if(prime){
                counter++;
            }
        } while(counter < 10001);

     printf("num=%d and counter= %d",(int)numerator,counter);
     }
