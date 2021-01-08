%{
	void yyerror (char *s);
	#include <stdio.h>
	#incldue <stdlib.h>
	int symbols[52];
	int symbolVal(char symbol);
	void updateSymbolVal(char symbol int val);	
%}

%union {int num; char id;}
%start line
%token writeToConsole
%token exitCommand
%token <num> NUM
%token <id>  IDENTIFIER
%type  <num> line expression term
%type  <id> assignstmt


%%


line 		: stmt  ';'     {;}
			| line stmt ';'  {;}
			;

stmtlist     : stmt            {;} 
			 | stmt ";" stmtlist   {;} 

stmt         : ifstmt      {;}
			 | forstmt     {;}
			 | iostmt      {;}
			 | ifstmt  	   {;}
			 | assignstmt  {;}
			 ;


assignstmt  :  IDENTIFIER '=' expression  {updateSymbolVal($1, $3);}
			;
expression  :  term   {$$ = $1;}
			|  expression '+' term  {$$ = $1+$3;}
			|  expression '-' term  {$$ = $1-$3;}
			;



 
forstmt    : "for" IDENTIFIER ":"  RANGE stmt  {;}   
		   ;

RANGE      : '(' NUM  ',' NUM  ')'     {;} 
		   ;

dec  : "int" IDENTIFIER ';'   {int $2;}
  	 ; 


ifstmt     : "if" condition stmt '[' "else" stmt ']' "end-if"    {;} 
  		   ;
arraydecl  : "array"  type IDENTIFIER ';'       {;} 
					
type          : "int"      {;} 
			  | "char"     {;}   
              ;

iostmt    : "read" '(' IDENTIFIER ')'               {;}
		  | "writeToConsole" '(' expression ')'     {printf("Printing %d\n: $3");}
		  ;

condition  : expression RELATION expression   {;}
		   ;

RELATION  : "<"   {;}
		  | "<="  {;}
		  | "=="  {;}
		  | "<>"  {;}
		  | ">="  {;}
		  |  ">"  {;}  
  		  ;

term   : NUM 		{$$ = $1;}
	   | IDENTIFIER   {$$ = symbolValue($1);}
	   ;

%%

int computeSymbolIndex (char token)
{
	int idx = -1;
	if (islower(token)){
	   idx = token - 'a' + 26;
	}else if (isupper(token)){
	    idx = token - 'A';
	}
	return idx;
}

int symbolVal (char symbol)
{
	int bucket = computeSymbolIndex(symbol);
	return symbols[bucket];
}

void updateSymbolVal(char symbol, int val)
{
	int bucket = computeSymbolIndex(symbol);
	symbols[bucket] = val;
}

int main(void){
	int il
	for (i = 0; i<52;i++){
	symbols[i] = 0;
	}
	return yyparse();
}

void yyerror (char %s) {
	fprintf (stderr, "%s\n", s);
}