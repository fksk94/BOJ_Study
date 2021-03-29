#include <iostream>

using namespace std;

int main()
{
    int m, left = 1, right, ea, mid, tmp;
    scanf("%d", &m);
    right = m*5;
    
    while (left <= right)
    {
        mid = (left+right)/2;
        ea = 0;
        tmp = mid;
        while (tmp >= 5)
        {
            ea += tmp/5;
            if (ea > m)
                break;
            tmp /= 5;
        }
        
        if (ea < m)
            left = mid+1;
        else
            right = mid-1;
    }
    
    ea = 0;
    tmp = left;
    
    while(tmp >= 5)
    {
        ea += tmp/5;
        tmp /= 5;
    }
    if (ea == m)
        printf("%d", left);
    else
        printf("-1");
    return 0;
}