#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char *convert(char *s, int numRows)
{
    int len = strlen(s);
    if (numRows <= 1 || len <= numRows)
    {
        return s;
    }
    char **rows = (char **)malloc(sizeof(char *) * numRows);
    memset(rows, 0, sizeof(char *) * numRows);
    for (int i = 0; i < numRows; i++)
    {
        rows[i] = (char *)malloc(sizeof(char) * (len + 1));
        rows[i][0] = '\0';
    }

    int curRow = 0, step = 1;
    for (int i = 0; i < len; i++)
    {
        int rowLen = strlen(rows[curRow]);
        rows[curRow][rowLen] = s[i];
        rows[curRow][rowLen + 1] = '\0';

        if (curRow == 0)
        {
            step = 1;
        }
        else if (curRow == numRows - 1)
        {
            step = -1;
        }
        curRow += step;
    }

    char *result = (char *)malloc(len + 1);
    result[0] = '\0';
    for (int i = 0; i < numRows; i++)
    {
        strcat(result, rows[i]);
        free(rows[i]);
    }
    free(rows);
    return result;
}

int main()
{
    char *s = "PAYPALISHIRING";
    int numRows = 3;
    char *result = convert(s, numRows);
    printf("%s\n", result);
}
