
/* 프로그램 5-1 중위식-후위식 변환 : infixtopostfix.c */
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <string.h>
#define MAX_STACK_SIZE 100 /* maximum stack size */
#define MAX_EXPR_SIZE 100 /* max size of expression */

//typedef enum {
//	lparen, rparen, plus, minus, times, divide,
//	mod, eos, operand
//} char;


char expr[MAX_EXPR_SIZE]; /* input string */
int top = -1;

char stack[MAX_STACK_SIZE];
/* isp and icp arrays ? index is value of char '(', rparen,
	plus, minus, times, divide, mode, eos */

void push(char item)
{
	if (top >= MAX_STACK_SIZE - 1) {
		printf("stack_full()\n");
		return;
	}
	stack[++top] = item;
}

char pop() {
	if (top == -1)
	{
		printf("stack_empty()\n");
	}
	return stack[(top)--];
}

int isempty()
{
	if (top == -1) return(1); else return(0);
}

int isfull()
{
	if (top >= MAX_STACK_SIZE - 1) return(1); else return(0);
}
static int isp[] = { 0,19,12,12,13,13,13,0 };
static int icp[] = { 20,19,12,12,13,13,13,0 }; // '(' 연산자 우선순위 조정

//int get_token(char* symbol, int* n) {
//	*symbol = expr[(*n)++];
//	switch (*symbol) {
//	case '(': return 0;
//	case ')': return 1;
//	case '+': return 2;
//	case '-': return 3;
//	case '/': return 4;
//	case '*': return 5;
//	case '%': return 6;
//	case ' ': return 7;
//	default: return 8;
//	}
//}

int get_token(char* symbol, int* n) {
	*symbol = expr[(*n)++];
	switch (*symbol) {
	case '(': return 0;
	case ')': return 1;
	case '+': return 2;
	case '-': return 3;
	case '/': return 4;
	case '*': return 5;
	case '%': return 6;
	case ' ': return 7;
	default: return 8;
	}
}

int symToInt(char symbol) {
	switch (symbol) {
	case '(': return 20;
	case ')': return 19;
	case '+': return 12;
	case '-': return 12;
	case '/': return 13;
	case '*': return 13;
	case '%': return 13;
	case ' ': return 0;
	default: return 8;
	}

}


char print_token(char t) {
	/*switch (t) {
	case 0: printf("( "); break;
	case 1: printf(") "); break;
	case 2: printf("+ "); break;
	case 3: printf("- "); break;
	case 4: printf("/ "); break;
	case 5: printf("* "); break;
	case 6: printf("% "); break;
	case 7: printf("eos "); break;
	default: printf("\n "); return(0);
	}*/
	printf("%d ", t);
	if (symToInt(t) == 8)
		printf("\n");
}

void postfix(void) {
	char symbol;
	char token;
	int n = 0;
	top = 0;
	stack[0] = ' '; // 스택의 바닥에 공백(eos)를 넣는다.
	for (token = get_token(&symbol, &n); token != 7; token = get_token(&symbol, &n))
	{
		if (token == 8) printf("%c ", symbol);
		else if (token == 1) {  // 오른쪽 괄호 만나면 스택에서 모두 pop..
			while (symToInt(stack[top]) != 20)
				print_token(pop());
			pop();
		}
		else { // 연산자들의 우선 순위 비교..
			while (symToInt(stack[top]) >= icp[token])
				print_token(pop()); 
			push(token);
		}
	}
	while ((token = pop()) != 7)
		print_token(token);
	printf(" \n");
}

int main()
{
	strcpy(expr, "3+2*5-4 "); // 입력의 마지막에 공백(eos)을 둔다.
	postfix();
}
