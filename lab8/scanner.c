#include <stdio.h>
#include "scanner.h"

extern int yylex();
extern int yylineno;
extern char *yytext;


char * names[] = {};

int main(void){
	
	int nameToken, valueToken;
	nameToken = yylex();
	while(nameToken){
		printf("%d\n", nameToken);
		nameToken = yylex();
	}
	return 0;
}