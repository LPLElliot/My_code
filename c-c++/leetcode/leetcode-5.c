#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int expand(char *s, int left, int right)
{
    int n = strlen(s);
    while (left >= 0 && right < n && s[left] == s[right])
    {
        left--;
        right++;
    }
    return right - left - 1;
}

char *longestPalindrome(char *s)
{
    if (s == NULL || strlen(s) < 1)
        return "";
    int n = strlen(s);
    int start = 0, max_len = 1;

    for (int i = 0; i < n; i++)
    {
        int len1 = expand(s, i, i);
        int len2 = expand(s, i, i + 1);
        int current_len = len1 > len2 ? len1 : len2;
        if (current_len > max_len)
        {
            max_len = current_len;
            start = i - (current_len - 1) / 2;
        }
    }

    char *result = (char *)malloc(max_len + 1);
    strncpy(result, s + start, max_len);
    result[max_len] = '\0';
    return result;
}

int main()
{
    char *test_cases[] = {
        "babad",
        "cbbd",
        "a",
        "aaaa",
        "abcde"};

    for (int i = 0; i < 5; i++)
    {
        char *input = test_cases[i];
        char *output = longestPalindrome(input);
        printf("输入: \"%s\"\t输出: \"%s\"\n", input, output);
        free(output);
    }
    return 0;
}
