#include <stdio.h>
#include <stdlib.h>
#define InitSize 10

//顺序表的定义
typedef struct {
	int *data;
	int MaxSize;
	int length;
} SqList;

//顺序表初始化
void InitList(SqList *L) {
	L->MaxSize = InitSize;
	L->data = (int *)malloc(L->MaxSize * sizeof(int));
	L->length = 5;
	for (int i = 0; i < L->length; i++) {
		L->data[i] = 0;
	}
}

//增加顺序表长度
void IncreaseSize(SqList *L, int len) {
	int *p = L->data;
	L->data = (int *)malloc((len + L->MaxSize) * sizeof(int));
	for (int i = 0; i < L->length; i++) {
		L->data[i] = p[i];
	}
	L->MaxSize += len;
	L->length += len;
	for (int i = 0; i < len; i++) {
		L->data[(L->length) + i - len] = 0;
	}
	free(p);
}

//插入
int ListInsert(SqList *L, int i, int e) {
	if (i < 1 || i > L->length + 1 || L->length >= L->MaxSize) {
		return 0;
	}
	for (int j = L->length; j >= i; j--) {
		L->data[j] = L->data[j - 1];
	}
	L->data[i - 1] = e;
	L->length++;
	return 1;
}

//删除
int ListDelete(SqList *L, int i, int *e) {
	if (i < 1 || i > L->length || L->length >= L->MaxSize) {
		return 0;
	}
	*e = L->data[i - 1];
	printf("删除了第%d个元素:%d\n", i - 1, *e);
	for (int j = i; j < L->length; j++) {
		L->data[j - 1] = L->data[j];
	}
	L->length--;
	return 1;
}

//按位查找
int GetElem(SqList *L, int i) {
	return L->data[i - 1];
}

//按值查找
int LocateElem(SqList *L, int e) {
	for (int i = 0; i <= L->length; i++) {
		if (L->data[i] == e) {
			return i + 1;
		}
	}
	return 0;
}

//输出顺序表
void PrintList(SqList *L) {
	for (int i = 0; i < L->length; i++) {
		printf("L[%d]=%d\n", i, L->data[i]);
	}
	printf("\n");
}

int main() {
	SqList L;
	int e = 0;
	//初始化
	InitList(&L);
	//在第3个位置插入5
	ListInsert(&L, 3, 5);
	PrintList(&L);
	//按位查找
	printf("第3位是%d\n\n", GetElem(&L, 3));
	//按值查找
	printf("5在第%d位\n\n", LocateElem(&L, 5));
	//删除第三个位置的数
	ListDelete(&L, 3, &e);
	PrintList(&L);
	return 0;
}
