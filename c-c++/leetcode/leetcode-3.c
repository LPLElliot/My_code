#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s)
{
    int max_len = 0;
    int left = 0;
    int last_pos[256];
    memset(last_pos, -1, sizeof(last_pos));

    for (int right = 0; s[right] != '\0'; right++)
    {
        if (last_pos[s[right]] >= left)
        {
            left = last_pos[s[right]] + 1;
        }
        last_pos[s[right]] = right;
        int current_len = right - left + 1;
        if (current_len > max_len)
        {
            max_len = current_len;
        }
    }
    return max_len;
}

int main()
{
    char s1[] = "abcabcbb";
    printf("%d\n", lengthOfLongestSubstring(s1));

    char s2[] = "bbbbb";
    printf("%d\n", lengthOfLongestSubstring(s2));

    char s3[] = "pwwkew";
    printf("%d\n", lengthOfLongestSubstring(s3));
    return 0;
}
