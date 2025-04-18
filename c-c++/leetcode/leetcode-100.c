#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct TreeNode
{
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isSameTree(struct TreeNode *p, struct TreeNode *q)
{
    if ((p == NULL && q != NULL) || (p != NULL && q == NULL))
        return false;
    else if (p == NULL && q == NULL)
        return true;
    else if (p->val != q->val)
        return false;
    else
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

int main()
{
    struct TreeNode *p = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    struct TreeNode *q = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    p->val = 1;
    p->left = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    p->left->val = 2;
    p->left->left = NULL;
    p->left->right = NULL;
    p->right = NULL;

    q->val = 1;
    q->left = NULL;
    q->right = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    q->right->val = 2;
    q->right->left = NULL;
    q->right->right = NULL;

    bool result = isSameTree(p, q);
    printf("%s\n", result ? "true" : "false");

    free(p->left);
    free(p->right);
    free(p);

    free(q->left);
    free(q->right);
    free(q);
    return 0;
}