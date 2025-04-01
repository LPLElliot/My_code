#include <stdio.h>

char *intToRoman(int num)
{
    if (!num)
        return "0";
    char *result = (char *)malloc(20 * sizeof(char));
    int i = 0;
    int denight = 0;
    while (num > 0)
    {
        denight = num % 10;
        num = num / 10;

        switch (denight)
        {
        case 1:
            result[i++] = 'I';
            break;
        case 2:
            result[i++] = 'II';
            break;
        case 3:
            result[i++] = 'III';
            break;
        case 4:
            result[i++] = 'IV';
            break;
        case 5:
            result[i++] = 'V';
            break;
        case 6:
            result[i++] = 'VI';
            break;
        case 7:
            result[i++] = 'VII';
            break;
        case 8:
            result[i++] = 'VIII';
            break;
        case 9:
            result[i++] = 'IX';
            break;
        }
    }
}