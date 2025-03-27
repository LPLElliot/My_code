#include <stdio.h>
#include <stdlib.h>

typedef struct LNode {
	int data;
	struct LNode *next;
} LNode, *LinkList;

//初始化带头结点的空单链表
int InitList(LinkList *L) {
	*L = (LNode*)malloc(sizeof(LNode));
	if (*L == NULL) return 0;
	(*L)->next = NULL;
	return 1;
}

//求链表长度
int Length(LinkList L) {
	int len = 0;
	LNode*p = L;
	while (p->next != NULL) {
		p = p->next;
		len++;
	}
	return len;
}

//按位查找
LNode*GetElem(LinkList L, int i) {
	if (i < 0) return NULL;
	int j = 0;
	LNode *p = L;
	while (p != NULL && j < i) {
		p = p->next;
		j++;
	}
	return p;
}

//按值查找
LNode*LocateElem(LinkList L, int e) {
	LNode*p = L->next;
	int n = 1;
	while (p != NULL && p->data != e) {
		p = p->next;
		n++;
	}
	if (p != NULL) {
		printf("%d在第%d位", e, n);
	}
	return p;
}

//带头结点插入
int ListInsert(LinkList L, int i, int e) {
	if (i < 1) return 0;
	LNode *p = GetElem(L, i - 1);
	if (p == NULL) return 0;
	LNode *s = (LNode*)malloc(sizeof(LNode));
	s->data = e;
	s->next = p->next;
	p->next = s;
	return 1;
}

//后插
int InsertNextNode(LNode *p, int e) {
	if (p == NULL) return 0;
	LNode *s = (LNode*)malloc(sizeof(LNode));
	if (s == NULL) return 0;
	s->data = e;
	s->next = p->next;
	p->next = s;
	return 1;
}

//前插
int InsertPriorNode(LNode *p, int e) {
	if (p == NULL) return 0;
	LNode *s = (LNode*)malloc(sizeof(LNode));
	if (s == NULL) return 0;
	s->next = p->next;
	p->next = s;
	s->data = p->data;
	p->data = e;
	return 1;
}

//按位删除
int ListDelete(LinkList L, int i, int* e) {
	if (i < 1) return 0;
	LNode*p = GetElem(L, i - 1);
	if (p == NULL) return 0;
	if (p->next == NULL) return 0;
	LNode* q = p->next;
	*e = q->data;
	printf("删除了第%d个元素%d\n", i, *e);
	p->next = q->next;
	free(q);
	return 1;
}

//指定节点删除
int DeleteNode(LNode *p) {
	if (p == NULL || p->next == NULL) return 0;
	LNode* q = p->next;
	p->data = q->data;
	p->next = q->next;
	free(q);
	return 1;
}

//尾插法建立
LinkList List_Taillnsert(LinkList L) {
	int x;
	LNode*s,*r = L;
	scanf("%d", &x);
	while (x != -1) {
		s = (LNode*)malloc(sizeof(LNode));
		s->data = x;
		r->next = s;
		r = s;
		scanf("%d", &x);
	}
	return L;
}

//头插法建立
LinkList List_HeadInsert(LinkList L) {
	int x;
	LNode*s;
	scanf("%d", &x);
	while (x != -1) {
		s = (LNode*)malloc(sizeof(LNode));
		s->data = x;
		s->next = L->next;
		L->next = s;
		scanf("%d", &x);
	}
	return L;
}

// 打印链表
void PrintList(LinkList L) {
	LNode *p = L->next;
	while (p != NULL) {
		printf("%d -> ", p->data);
		p = p->next;
	}
	printf("NULL\n");
}

int main() {
	LinkList L;
	InitList(&L);
	//List_Taillnsert(L);
	List_HeadInsert(L);
	printf("初始后链表：");
	PrintList(L);
	ListInsert(L, 1, 10);
	ListInsert(L, 1, 20);
	ListInsert(L, 3, 30);
	printf("插入后链表：");
	PrintList(L);
	printf("表长:%d\n", Length(L));
	LNode *firstNode = L->next;
	InsertNextNode(firstNode, 30);
	printf("后插后链表：");
	PrintList(L);
	InsertPriorNode(firstNode, 10);
	printf("前插后链表：");
	PrintList(L);
	int e = 0;
	ListDelete(L, 3, &e);
	printf("删除后链表：");
	PrintList(L);
	DeleteNode(firstNode->next);
	printf("删除第二个结点后链表：");
	PrintList(L);
	printf("按位查找第二个结点是：%d\n", GetElem(L, 2)->data);
	printf("(按值查找%d)\n", LocateElem(L, 30)->data);
	return 0;
}
