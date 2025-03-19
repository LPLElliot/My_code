#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 辅助函数：从中心向两侧扩展，返回回文长度
int expand(char* s, int left, int right) {
    int n = strlen(s);
    while (left >= 0 && right < n && s[left] == s[right]) {
        left--;
        right++;
    }
    return right - left - 1; // 实际回文长度为 right-left-1
}

// 主函数：寻找最长回文子串
char* longestPalindrome(char* s) {
    if (s == NULL || strlen(s) < 1) return "";
    int n = strlen(s);
    int start = 0, max_len = 1; // 初始长度为1（单个字符）

    for (int i = 0; i < n; i++) {
        // 奇数长度回文（中心为i）
        int len1 = expand(s, i, i);
        // 偶数长度回文（中心为i和i+1）
        int len2 = expand(s, i, i + 1);
        // 取当前中心的最长回文
        int current_len = len1 > len2 ? len1 : len2;
        if (current_len > max_len) {
            max_len = current_len;
            start = i - (current_len - 1) / 2; // 计算起始位置
        }
    }

    // 动态分配内存存储结果
    char* result = (char*)malloc(max_len + 1);
    strncpy(result, s + start, max_len);
    result[max_len] = '\0';
    return result;
}

// 测试函数
int main() {
    // 测试用例
    char* test_cases[] = {
        "babad",  // 预期: "bab" 或 "aba"
        "cbbd",    // 预期: "bb"
        "a",       // 预期: "a"
        "aaaa",    // 预期: "aaaa"
        "abcde"    // 预期: "a"
    };

    for (int i = 0; i < 5; i++) {
        char* input = test_cases[i];
        char* output = longestPalindrome(input);
        printf("输入: \"%s\"\t输出: \"%s\"\n", input, output);
        free(output); // 释放内存
    }
    return 0;
}
