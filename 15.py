#include<stdio.h>
int main()
{
    int s,r,t;
    scanf("%d%d",&r,&t);
    if(r<=100000&&t<=100000)
    {
    for(s=r+1;s<t;s++)
    {
        if(s%2==0)
            printf("%d  ",s);
    }

    }
}
