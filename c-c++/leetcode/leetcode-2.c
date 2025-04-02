#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    typedef struct ListNode ListNode;
    ListNode *dummy = (ListNode *)malloc(sizeof(ListNode));
    dummy->val = 0;
    dummy->next = NULL;
    ListNode *p = dummy;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry)
    {
        ListNode *node = (ListNode *)malloc(sizeof(ListNode));
        node->val = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
        carry = node->val / 10;
        node->val %= 10;

        node->next = NULL;
        p->next = node;
        p = node;

        if (l1)
            l1 = l1->next;
        if (l2)
            l2 = l2->next;
    }
    ListNode *head = dummy->next;
    free(dummy);
    return head;
}

void freeList(struct ListNode *head)
{
    struct ListNode *tmp;
    while (head != NULL)
    {
        tmp = head;
        head = head->next;
        free(tmp);
    }
}

int main()
{
    struct ListNode *l1 = (struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *l2 = (struct ListNode *)malloc(sizeof(struct ListNode));
    l1->val = 9;
    l1->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    l1->next->val = 9;
    l1->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    l1->next->next->val = 9;
    l1->next->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    l1->next->next->next->val = 9;
    l1->next->next->next->next = NULL;

    l2->val = 9;
    l2->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    l2->next->val = 9;
    l2->next->next = (struct ListNode *)malloc(sizeof(struct ListNode));
    l2->next->next->val = 9;
    l2->next->next->next = NULL;

    struct ListNode *result = addTwoNumbers(l1, l2);
    while (result != NULL)
    {
        printf("%d ", result->val);
        result = result->next;
    }
    printf("\n");

    freeList(l1);
    freeList(l2);
    freeList(result);
    return 0;
}