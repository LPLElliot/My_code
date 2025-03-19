#include <stdio.h>
#include <stdlib.h>

typedef struct DNode
{
	int data;
	struct DNode *prior, *next;
} DNode, *DLinklist;

// 初始化带头结点的空双链表
int InitDLinkList(DLinklist *L)
{
	*L = (DNode *)malloc(sizeof(DNode));
	if (*L == NULL)
		return 0;
	(*L)->prior = NULL;
	(*L)->next = NULL;
	return 1;
}

// 求双链表长度
int Length(DLinklist L)
{
	int len = 0;
	DNode *p = L->next;
	while (p != NULL)
	{
		p = p->next;
		len++;
	}
	return len;
}

// 按位查找（返回第i个结点，头结点算第0个）
DNode *GetElem(DLinklist L, int i)
{
	if (i < 0)
		return NULL;
	DNode *p = L;
	int j = 0;
	while (p != NULL && j < i)
	{
		p = p->next;
		j++;
	}
	return p;
}

// 按值查找（返回第一个等于e的结点）
DNode *LocateElem(DLinklist L, int e)
{
	DNode *p = L->next;
	while (p != NULL && p->data != e)
	{
		p = p->next;
	}
	return p;
}

// 在p结点后插入元素e（封装创建结点过程）
int InsertNextDNode(DNode *p, int e)
{
	if (p == NULL)
		return 0;
	DNode *s = (DNode *)malloc(sizeof(DNode));
	if (s == NULL)
		return 0;
	s->data = e;
	s->next = p->next;
	s->prior = p;
	if (p->next != NULL)
	{ // 如果p不是尾结点
		p->next->prior = s;
	}
	p->next = s;
	return 1;
}

// 在p结点前插入元素e（封装创建结点过程）
int InsertPriorDNode(DNode *p, int e)
{
	if (p == NULL)
		return 0;
	DNode *s = (DNode *)malloc(sizeof(DNode));
	if (s == NULL)
		return 0;
	s->data = e;
	s->prior = p->prior;
	s->next = p;
	if (p->prior != NULL)
	{ // 如果p不是首元结点
		p->prior->next = s;
	}
	p->prior = s;
	return 1;
}

// 按位插入（在第i个位置插入e）
int ListInsert(DLinklist L, int i, int e)
{
	if (i < 1)
		return 0;
	DNode *p = GetElem(L, i - 1); // 找前驱结点
	return InsertNextDNode(p, e);
}

// 删除p结点的后继结点
int DeleteNextDNode(DNode *p)
{
	if (p == NULL || p->next == NULL)
		return 0;
	DNode *q = p->next;
	p->next = q->next;
	if (q->next != NULL)
	{
		q->next->prior = p;
	}
	free(q);
	return 1;
}

// 按位删除（删除第i个结点）
int ListDelete(DLinklist L, int i, int *e)
{
	if (i < 1)
		return 0;
	DNode *p = GetElem(L, i); // 直接定位到目标结点
	if (p == NULL)
		return 0;
	*e = p->data;
	p->prior->next = p->next;
	if (p->next != NULL)
	{
		p->next->prior = p->prior;
	}
	free(p);
	return 1;
}

// 尾插法建立双链表
DLinklist List_TailInsert(DLinklist L)
{
	int x;
	DNode *r = L; // 尾指针
	scanf("%d", &x);
	while (x != -1)
	{
		DNode *s = (DNode *)malloc(sizeof(DNode));
		s->data = x;
		s->prior = r;
		r->next = s;
		r = s;
		scanf("%d", &x);
	}
	r->next = NULL; // 尾结点next置空
	return L;
}

// 头插法建立双链表
DLinklist List_HeadInsert(DLinklist L)
{
	int x;
	scanf("%d", &x);
	while (x != -1)
	{
		DNode *s = (DNode *)malloc(sizeof(DNode));
		s->data = x;
		s->next = L->next;
		s->prior = L;
		if (L->next != NULL)
		{ // 原首元结点存在时更新其prior
			L->next->prior = s;
		}
		L->next = s;
		scanf("%d", &x);
	}
	return L;
}

// 打印双链表
void PrintList(DLinklist L)
{
	DNode *p = L->next;
	printf("NULL <-> ");
	while (p != NULL)
	{
		printf("%d <-> ", p->data);
		p = p->next;
	}
	printf("NULL\n");
}

int main()
{
	DLinklist L;
	InitDLinkList(&L);

	// 测试尾插法
	printf("尾插法输入元素（-1结束）:");
	List_TailInsert(L);
	printf("尾插法结果：");
	PrintList(L);

	// 测试头插法
	printf("头插法输入元素（-1结束）:");
	List_HeadInsert(L);
	printf("头插法结果：");
	PrintList(L);

	// 测试插入
	ListInsert(L, 1, 10);
	ListInsert(L, 1, 20);
	ListInsert(L, 3, 30);
	printf("插入后链表：");
	PrintList(L);

	// 测试删除
	int e;
	ListDelete(L, 2, &e);
	printf("删除第2个元素%d后：", e);
	PrintList(L);

	// 测试查找
	DNode *p = GetElem(L, 3);
	printf("第3个元素是：%d\n", p->data);
	p = LocateElem(L, 30);
	printf("元素30的地址：%p\n", p);

	return 0;
}
