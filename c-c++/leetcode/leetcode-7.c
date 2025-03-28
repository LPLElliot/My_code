#include <stdio.h>

int reverse(int x)
{
    long res = 0;
    while (x != 0)
    {
        res = res * 10 + x % 10;
        if ((int)res != res)
            return 0;
        x /= 10;
    }
    return res;
}

int main()
{
    int x = 1534236469;
    printf("%d\n", reverse(x));
    return 0;
}