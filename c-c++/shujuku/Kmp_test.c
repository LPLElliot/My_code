#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

// GetNext 函数：计算模式串 p 的 next 数组
// p：模式串
// next：存储 next 数组的数组
void GetNext(char *p, int next[])
{
    int pLen = strlen(p); // 计算模式串 p 的长度
    next[0] = -1;         // 初始化 next[0] 为 -1，表示如果第一个字符不匹配，则主串指针后移
    int k = -1;           // k 表示当前最长公共前后缀的长度，初始化为 -1
    int j = 0;            // j 表示当前要计算 next 值的字符的位置，初始化为 0
    while (j < pLen - 1)  // 循环直到计算完所有 next 值（除了最后一个字符）
    {
        // 如果 k == -1，表示当前没有公共前后缀，或者 p[j] == p[k]，表示可以扩展公共前后缀
        if (k == -1 || p[j] == p[k])
        {
            ++j;              // j 后移
            ++k;              // k 后移
            if (p[j] != p[k]) // 如果 p[j] != p[k]，表示 next[j] = k
                next[j] = k;
            else // 如果 p[j] == p[k]，表示 next[j] = next[k]，因为如果 p[j] == p[k]，那么当 p[j] 匹配失败时，应该回溯到 next[k] 的位置，而 next[k] 已经知道应该回溯到哪里了
                next[j] = next[k];
        }
        else
        {
            k = next[k]; // 如果 p[j] != p[k]，且 k != -1，表示无法扩展公共前后缀，需要回溯 k
        }
    }
}

// KMP 函数：在主串 s 中查找模式串 p 的位置
// s：主串
// p：模式串
// pos：查找的起始位置
int KMP(char *s, char *p, int pos)
{
    int i = pos;                 // i 表示主串 s 的当前位置，初始化为 pos
    int j = 0;                   // j 表示模式串 p 的当前位置，初始化为 0
    int sLen = strlen(s);        // 计算主串 s 的长度
    int pLen = strlen(p);        // 计算模式串 p 的长度
    int next[pLen];              // 定义 next 数组，用于存储模式串 p 的 next 值
    GetNext(p, next);            // 计算模式串 p 的 next 值
    while (i < sLen && j < pLen) // 循环直到主串或模式串到达末尾
    {
        // 如果 j == -1，表示模式串从头开始匹配，或者 s[i] == p[j]，表示当前字符匹配成功
        if (j == -1 || s[i] == p[j])
        {
            ++i; // 主串指针后移
            ++j; // 模式串指针后移
        }
        else
        {
            j = next[j]; // 如果当前字符匹配失败，则模式串指针回溯到 next[j] 的位置
        }
    }
    if (j == pLen)    // 如果 j == pLen，表示模式串已经完全匹配
        return i - j; // 返回模式串在主串中的起始位置
    else
        return -1; // 如果 i == sLen，表示主串已经到达末尾，但模式串没有完全匹配，返回 -1
}

// 暴力匹配函数：在主串 s 中查找模式串 p 的位置
// s：主串
// p：模式串
// pos：查找的起始位置
int BruteForce(char *s, char *p, int pos)
{
    int i = pos;                 // i 表示主串 s 的当前位置，初始化为 pos
    int j = 0;                   // j 表示模式串 p 的当前位置，初始化为 0
    int sLen = strlen(s);        // 计算主串 s 的长度
    int pLen = strlen(p);        // 计算模式串 p 的长度
    while (i < sLen && j < pLen) // 循环直到主串或模式串到达末尾
    {
        if (s[i] == p[j]) // 如果当前字符匹配成功
        {
            ++i; // 主串指针后移
            ++j; // 模式串指针后移
        }
        else
        {
            i = i - j + 1; // 如果当前字符匹配失败，则主串指针回溯到 i - j + 1 的位置
            j = 0;         // 模式串指针重置为 0
        }
    }
    if (j == pLen)    // 如果 j == pLen，表示模式串已经完全匹配
        return i - j; // 返回模式串在主串中的起始位置
    else
        return -1; // 如果 i == sLen，表示主串已经到达末尾，但模式串没有完全匹配，返回 -1
}

// 主函数
int main()
{
    // 生成随机字符串
    int sLen = 20;
    int pLen = 5;
    char *s = (char *)malloc(sizeof(char) * (sLen + 1));
    char *p = (char *)malloc(sizeof(char) * (pLen + 1));
    srand(time(NULL));
    for (int i = 0; i < sLen; i++)
    {
        s[i] = 'a' + rand() % 26;
    }
    s[sLen] = '\0';
    for (int i = 0; i < pLen; i++)
    {
        p[i] = 'a' + rand() % 26;
    }
    p[pLen] = '\0';

    // KMP 算法
    clock_t start = clock();
    int posKMP = KMP(s, p, 0);
    clock_t end = clock();
    double timeKMP = (double)(end - start) / CLOCKS_PER_SEC;

    // 暴力匹配算法
    start = clock();
    int posBruteForce = BruteForce(s, p, 0);
    end = clock();
    double timeBruteForce = (double)(end - start) / CLOCKS_PER_SEC;

    printf("主串长度: %d, 模式串长度: %d\n", sLen, pLen);
    printf("KMP 算法结果: pos = %d, time = %f\n", posKMP, timeKMP);
    printf("暴力匹配算法结果: pos = %d, time = %f\n", posBruteForce, timeBruteForce);

    free(s);
    free(p);

    return 0;
}