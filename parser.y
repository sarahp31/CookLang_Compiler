%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern int yylex();
void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}

%token NUMBER STRING WORD COMENTARIO INGREDIENTE PASSO LEFT_PARENTHESIS RIGHT_PARENTHESIS PRE_AQUECER_FORNO MISTURAR ADICIONAR MISTURAR_POR ASSAR UNIDADE IDENTATION BREAKLINE SPACE COMMA

%start recipe

%%
recipe:
    header BREAKLINE ingredient_list BREAKLINE step_list
    ;

header:
    COMENTARIO SPACE title_line 
    ;

title_line:
    title
    | title_line SPACE title
    ;

title:
    WORD
    ;


ingredient_list:
    ingredient
    | ingredient_list BREAKLINE ingredient
    ;

ingredient:
    INGREDIENTE SPACE WORD SPACE NUMBER SPACE UNIDADE
    ;

step_list:
    | step_list BREAKLINE step
    ;

step:
    PASSO SPACE action
    ;

action:
    PRE_AQUECER_FORNO LEFT_PARENTHESIS NUMBER COMMA NUMBER RIGHT_PARENTHESIS
    | MISTURAR LEFT_PARENTHESIS ingredients RIGHT_PARENTHESIS
    | ADICIONAR LEFT_PARENTHESIS ingredients RIGHT_PARENTHESIS
    | ASSAR LEFT_PARENTHESIS NUMBER COMMA NUMBER RIGHT_PARENTHESIS
    ;

ingredients:
    WORD
    | ingredients COMMA WORD
    | ingredients COMMA  SPACE WORD
    ;

%%

int main() {
    yyparse();
    return 0;
}
