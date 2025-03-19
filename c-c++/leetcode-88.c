#include <stdio.h>

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
   int p1 = m - 1;
   int p2 = n - 1;
   int p = m + n - 1;
   while (p1 >= 0 && p2 >= 0)
   {
      if (nums1[p1] > nums2[p2])
      {
         nums1[p] = nums1[p1];
         p1--;
      }
      else
      {
         nums1[p] = nums2[p2];
         p2--;
      }
      p--;
   }
   while (p2 >= 0)
   {
      nums1[p] = nums2[p2];
      p2--;
      p--;
   }
}

int main()
{
   int nums1[6] = {2, 5, 6, 0, 0, 0};
   int nums2[3] = {1, 2, 3};
   merge(nums1, 6, 3, nums2, 3, 3);
   for (int i = 0; i < 6; i++)
   {
      printf("%d ", nums1[i]);
   }
   return 0;
}