#include<stdio.h>

int main()
{

int a,b,flag=0;

for(a=1; ; a++)
{
    for(b=1; b<=20; b++)
    {
        if (a%b==0)
            {
                flag++;
            }

    }
    if (flag==20)
        {
            printf("The least num divisible by 1 to 20 is = %d",a);
            break;
        }
        flag=0;
}


return 0;
}

