#include <stdio.h>
#include <string.h>

void GetNext(char *p, int next[])
{
    int pLen = strlen(p);
    next[0] = -1;
    int k = -1;
    int j = 0;
    while (j < pLen - 1)
    {
        if (k == -1 || p[j] == p[k])
        {
            ++j;
            ++k;
            if (p[j] != p[k])
                next[j] = k;
            else
                next[j] = next[k];
        }
        else
        {
            k = next[k];
        }
    }
}

int KMP(char *s, char *p, int pos)
{
    int i = pos;
    int j = 0;
    int sLen = strlen(s);
    int pLen = strlen(p);
    int next[pLen];
    GetNext(p, next);
    while (i < sLen && j < pLen)
    {
        if (j == -1 || s[i] == p[j])
        {
            ++i;
            ++j;
        }
        else
        {
            j = next[j];
        }
    }
    if (j == pLen)
        return i - j;
    else
        return -1;
}
int main()
{
    char s[] = "ababcabcacbab";
    char p[] = "abcac";
    int pos = KMP(s, p, 0) + 1;
    printf("%d\n", pos);
    return 0;
}