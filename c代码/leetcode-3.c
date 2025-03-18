#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char *s) {
    int max_len = 0;
    int left = 0;  // 窗口左边界
    int last_pos[256];  // 哈希表：记录字符最后出现的位置（ASCII共256个字符）
    memset(last_pos, -1, sizeof(last_pos));  // 初始化为-1

    for (int right = 0; s[right] != '\0'; right++) {
        // 如果字符在窗口内已存在，移动左边界
        if (last_pos[s[right]] >= left) {
            left = last_pos[s[right]] + 1;
        }
        // 更新字符的最新位置
        last_pos[s[right]] = right;
        // 计算当前窗口长度，更新最大值
        int current_len = right - left + 1;
        if (current_len > max_len) {
            max_len = current_len;
        }
    }
    return max_len;
}

int main() {
    char s1[] = "abcabcbb";
    printf("%d\n", lengthOfLongestSubstring(s1));  // 输出: 3（"abc"）

    char s2[] = "bbbbb";
    printf("%d\n", lengthOfLongestSubstring(s2));  // 输出: 1（"b"）

    char s3[] = "pwwkew";
    printf("%d\n", lengthOfLongestSubstring(s3));  // 输出: 3（"wke"）
    return 0;
}
