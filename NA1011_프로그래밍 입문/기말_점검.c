#include <stdio.h>
int print(int n){
	int i;
	if (n > 0) print(n-1);
	if(n != 0) printf("%d\n", n);
}
	
int main(void){
    int n = 0;
    printf("정수를 입력해 주세요");
	scanf("%d", &n);
    print(n);
    
}