#include <stdio.h>
#define Min(a, b) ((a) < (b) ? (a) : (b))
#define Max(a, b) ((a) > (b) ? (a) : (b))

int maxArea(int *height, int heightSize)
{
    if (heightSize < 2)
        return 0;
    if (heightSize == 2)
        return Min(height[0], height[1]) * 1;
    int area = 0;
    int left = 0, right = heightSize - 1;
    while (left < right)
    {
        area = Max(Min(height[left], height[right]) * (right - left), area);
        if (height[left] < height[right])
            left++;
        else
            right--;
    }
    return area;
}

int main()
{
    int height[] = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int heightSize = sizeof(height) / sizeof(height[0]);
    printf("Max area: %d\n", maxArea(height, heightSize));
    return 0;
}