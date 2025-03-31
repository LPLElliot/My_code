#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

int myAtoi(char *s)
{
    if (s == NULL)
        return 0;

    int i = 0;
    int sign = 1;
    long long result = 0;

    while (s[i] == ' ')
        i++;

    if (s[i] == '-' || s[i] == '+')
    {
        sign = (s[i] == '-') ? -1 : 1;
        i++;
    }

    while (s[i] >= '0' && s[i] <= '9')
    {
        int digit = s[i] - '0';

        if (result > (LLONG_MAX / 10))
        {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }

        if (result == (LLONG_MAX / 10) && digit > (INT_MAX % 10))
        {
            return (sign == 1) ? INT_MAX : INT_MIN;
        }

        result = result * 10 + digit;
        i++;

        if (result * sign >= INT_MAX)
        {
            return INT_MAX;
        }
        if (result * sign <= INT_MIN)
        {
            return INT_MIN;
        }
    }

    return (int)(result * sign);
}

int main()
{
    char *s = "-91283472332 ";
    printf("%d\n", myAtoi(s));
    return 0;
}