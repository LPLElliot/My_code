#include <stdio.h>
#include <stdlib.h>

#define MaxSize 10

typedef struct
{
	int *data;
	int front, rear;
} SqQueue;

int main()
{
	SqQueue Q;
	Q.data = (int *)malloc(MaxSize * sizeof(int));
	Q.front = Q.rear = 0;
	return 0;
}
