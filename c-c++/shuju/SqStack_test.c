#include <stdio.h>
#include <stdlib.h>

#define MaxSize 10

typedef struct {
	int *data;
	int top;
} SqStack;

// 初始化栈
void InitStack(SqStack *S) {
	S->top = -1;  // 初始化为-1表示空栈
	S->data = (int*)malloc(sizeof(int) * MaxSize);
	if (!S->data) {
		fprintf(stderr, "内存分配失败\n");
		exit(1);
	}
}

// 入栈
int Push(SqStack *S, int x) {
	if (S->top == MaxSize - 1) return 0; // 栈满
	S->data[++S->top] = x;  // 先自增top，再赋值
	return 1;
}

// 出栈
int Pop(SqStack *S, int *x) {
	if (S->top == -1) return 0; // 栈空
	*x = S->data[S->top--];     // 先取数据，再自减top
	return 1;
}

// 读取栈顶
int GetTop(SqStack *S, int *x) {
	if (S->top == -1) return 0;
	*x = S->data[S->top];
	return 1;
}

int main() {
	SqStack S;        // 声明栈对象（非指针）
	InitStack(&S);    // 传递一级指针
	
	// 入栈1~10
	for (int i = 1; i <= 10; i++) {
		if (!Push(&S, i)) {
			printf("栈满，无法入栈 %d\n", i);
		}
	}
	
	
	// 出栈并打印
	int b[10] = {0};
	for (int i = 0; i < 10; i++) {  // 索引从0开始
		if (Pop(&S, &b[i])) {
			printf("%d ", b[i]);
		}
	}
	int a = 0;
	GetTop(&S, &a);
	printf("\n栈顶元素:%d\n", a);
	
	// 释放动态内存
	free(S.data);
	return 0;
}
