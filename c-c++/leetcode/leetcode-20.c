#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isValid(char *s)
{
    int len = strlen(s);
    if (len % 2 != 0)
        return false;

    char stack[10000];
    int top = -1;

    for (int i = 0; i < len; i++)
    {
        char c = s[i];
        if (c == '(' || c == '[' || c == '{')
        {
            stack[++top] = c;
        }
        else
        {
            if (top == -1)
                return false;

            char top_char = stack[top--];
            if ((c == ')' && top_char != '(') ||
                (c == ']' && top_char != '[') ||
                (c == '}' && top_char != '{'))
            {
                return false;
            }
        }
    }
    return top == -1;
}

typedef struct
{
    char *input;
    bool expected;
} TestCase;

int main()
{
    TestCase tests[] = {
        {"", true}, {"()", true}, {"()[]{}", true}, {"{[()]}", true}, {"(", false}, {")", false}, {"(]", false}, {"([)]", false}, {"(((((())))))", true}, {"()([]{})[]", true}, {"(()))", false}, {"(((()", false}, {"}{}{", false}, {")()(", false}};

    int total = sizeof(tests) / sizeof(tests[0]);
    int passed = 0;

    for (int i = 0; i < total; i++)
    {
        bool result = isValid(tests[i].input);
        const char *status = (result == tests[i].expected) ? "✓" : "✗";

        passed += (result == tests[i].expected) ? 1 : 0;

        printf("Test %2d %s | Input: \"%-12s\" | Expected: %-5s | Actual: %-5s\n",
               i + 1, status, tests[i].input,
               tests[i].expected ? "true" : "false",
               result ? "true" : "false");
    }

    printf("\nPassed %d/%d tests (%.0f%%)\n", passed, total, (float)passed / total * 100);
    return (passed == total) ? 0 : 1;
}
