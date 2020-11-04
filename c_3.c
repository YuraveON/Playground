#include <stdio.h>

int main(){
    int a,b,c;
    printf("Masukan nilai a: "); 
    scanf("%d", &a);
    printf("Masukan nilai b: "); 
    scanf("%d", &b);
    c=a+b;
    printf("Hasil %d + %d = %d\n",a,b,c);
    return 0;
}