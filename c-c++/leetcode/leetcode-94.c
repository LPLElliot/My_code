#include <stdio.h>
#include <stdlib.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

void inorder(struct TreeNode *root, int *res, int *resSize)
{
    if (!root)
    {
        return;
    }
    inorder(root->left, res, resSize);
    res[(*resSize)++] = root->val;
    inorder(root->right, res, resSize);
}

int *inorderTraversal(struct TreeNode *root, int *returnSize)
{
    int *res = malloc(sizeof(int) * 100);
    *returnSize = 0;
    inorder(root, res, returnSize);
    return res;
}

int main()
{
    struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    root->left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->left->val = 2;
    root->left->left = NULL;
    root->left->right = NULL;
    root->right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->right->val = 3;
    root->right->left = NULL;
    root->right->right = NULL;
    int returnSize = 0;
    int *result = inorderTraversal(root, &returnSize);
    for (int i = 0; i < returnSize; i++)
        printf("%d ", result[i]);
    printf("\n");
    free(result);
    free(root->left);
    free(root->right);
    free(root);
    return 0;
}