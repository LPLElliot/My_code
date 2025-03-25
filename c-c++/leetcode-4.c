#include <stdio.h>

double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    if (nums1Size == 0 && nums2Size == 0)
        return 0.0;
    if (nums1Size == 0)
    {
        if (nums2Size % 2 == 0)
        {
            return (nums2[nums2Size / 2] + nums2[nums2Size / 2 - 1]) / 2.0;
        }
        else
        {
            return nums2[nums2Size / 2];
        }
    }
    else if (nums2Size == 0)
    {
        if (nums1Size % 2 == 0)
        {
            return (nums1[nums1Size / 2] + nums1[nums1Size / 2 - 1]) / 2.0;
        }
        else
        {
            return nums1[nums1Size / 2];
        }
    }
    int totalSize = nums1Size + nums2Size;
    int tmp[totalSize];
    int i = 0, j = 0, k = 0;
    while (i < nums1Size && j < nums2Size)
    {
        if (nums1[i] <= nums2[j])
        {
            tmp[k] = nums1[i];
            i++;
            k++;
        }
        else
        {
            tmp[k] = nums2[j];
            j++;
            k++;
        }
    }
    if (i < nums1Size)
    {
        for (; i < nums1Size; i++)
        {
            tmp[k] = nums1[i];
            k++;
        }
    }
    if (j < nums2Size)
    {
        for (; j < nums2Size; j++)
        {
            tmp[k] = nums2[j];
            k++;
        }
    }
    if (totalSize % 2 == 0)
    {
        return (tmp[totalSize / 2] + tmp[totalSize / 2 - 1]) / 2.0;
    }
    else
    {
        return tmp[totalSize / 2];
    }
}

int main()
{
    int nums1[] = {1, 3, 5, 7, 9, 10};
    int nums2[] = {};
    printf("%f\n", findMedianSortedArrays(nums1, 6, nums2, 0));
    return 0;
}