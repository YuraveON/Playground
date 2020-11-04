#include <stdio.h>


int main(){
/* VOLUME BALOK */
int p,l,t,v;
printf("Masukan panjang (cm): ");
scanf("%d", &p);
printf("Masukan lebar (cm): ");
scanf("%d", &l);
printf("Masukan tinggi (cm): ");
scanf("%d", &t);

v = p*l*t;

printf("Volume balok dengan panjang %d cm, lebar %d cm, dan tinggi %d cm adalah %d cm^3\n", p,l,t,v);
return 0;
}
