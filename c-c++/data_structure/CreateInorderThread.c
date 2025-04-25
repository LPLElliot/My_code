#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ThreadedNode
{
    int data;
    struct ThreadedNode *left;
    struct ThreadedNode *right;
    bool ltag; // 左标志位：false 表示指向左子树，true 表示指向前驱
    bool rtag; // 右标志位：false 表示指向右子树，true 表示指向后继
} typedef ThreadedNode;

void initThreadedNode(ThreadedNode *node, int data)
{
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    node->ltag = false;
    node->rtag = false;
}

void visit(ThreadedNode *node)
{
    if (node != NULL)
    {
        printf("%d ", node->data);
    }
}

// 中序线索化辅助函数
void InorderThreading(ThreadedNode *node, ThreadedNode **pre)
{
    if (node == NULL)
        return;

    // 递归处理左子树
    InorderThreading(node->left, pre);

    // 处理当前节点
    if (node->left == NULL)
    {
        node->ltag = true; // 左指针改为线索
        node->left = *pre; // 指向前驱
    }
    if (*pre != NULL && (*pre)->right == NULL)
    {
        (*pre)->rtag = true;  // 右指针改为线索
        (*pre)->right = node; // 前驱的右指针指向当前节点
    }
    *pre = node; // 更新前驱为当前节点

    // 递归处理右子树
    InorderThreading(node->right, pre);
}

// 中序线索化入口函数
void CreateInorderThread(ThreadedNode *root)
{
    ThreadedNode *pre = NULL;
    InorderThreading(root, &pre);
    if (pre != NULL)
    {
        pre->rtag = true; // 最后一个节点的右指针指向 NULL
        pre->right = NULL;
    }
}

// 中序遍历线索二叉树
void InorderTraversalThreaded(ThreadedNode *root)
{
    ThreadedNode *node = root;
    while (node != NULL)
    {
        // 找到第一个中序节点
        while (node->ltag == false)
        {
            node = node->left;
        }
        visit(node);

        // 按线索访问后继节点
        while (node->rtag == true && node->right != NULL)
        {
            node = node->right;
            visit(node);
        }

        // 转向右子树
        node = node->right;
    }
}

int main()
{
    ThreadedNode *root = (ThreadedNode *)malloc(sizeof(ThreadedNode));
    initThreadedNode(root, 1);
    root->left = (ThreadedNode *)malloc(sizeof(ThreadedNode));
    initThreadedNode(root->left, 2);
    root->right = (ThreadedNode *)malloc(sizeof(ThreadedNode));
    initThreadedNode(root->right, 3);
    root->left->left = (ThreadedNode *)malloc(sizeof(ThreadedNode));
    initThreadedNode(root->left->left, 4);
    root->left->right = (ThreadedNode *)malloc(sizeof(ThreadedNode));
    initThreadedNode(root->left->right, 5);

    // 中序线索化
    CreateInorderThread(root);

    // 遍历线索二叉树
    printf("Inorder Traversal of Threaded Binary Tree: ");
    InorderTraversalThreaded(root);
    printf("\n");

    // 释放内存
    free(root->left->right);
    free(root->left->left);
    free(root->right);
    free(root->left);
    free(root);

    return 0;
}