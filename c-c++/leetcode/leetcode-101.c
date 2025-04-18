#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isSy(struct TreeNode *left, struct TreeNode *right)
{
    if (left == NULL && right == NULL)
        return true;
    else if (left == NULL || right == NULL)
        return false;
    else
    {
        if (left->val != right->val)
            return false;
        else
        {
            return isSy(left->left, right->right) && isSy(left->right, right->left);
        }
    }
}

bool isSymmetric(struct TreeNode *root)
{
    if (root == NULL)
        return true;
    return isSy(root->left, root->right);
}

int main()
{
    struct TreeNode *root = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->val = 1;
    root->left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->left->val = 2;
    root->right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->right->val = 2;
    root->left->left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->left->left->val = 3;
    root->left->right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->left->right->val = 4;
    root->right->left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->right->left->val = 4;
    root->right->right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    root->right->right->val = 3;
    root->left->left->left = NULL;
    root->left->left->right = NULL;
    root->left->right->left = NULL;
    root->left->right->right = NULL;
    root->right->left->left = NULL;
    root->right->left->right = NULL;
    root->right->right->left = NULL;
    root->right->right->right = NULL;

    if (isSymmetric(root))
        printf("true\n");
    else
        printf("false\n");

    free(root->left);
    free(root->right);
    free(root);

    return 0;
}