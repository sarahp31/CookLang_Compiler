%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.tab.h"
%}

DIGIT [0-9]
LETTER [a-zA-Z]

%%

"\t"|"    "  { printf("IDENTATION\n"); return IDENTATION; }
" " { printf("SPACE\n"); return SPACE; }
"\n" { printf("BREAKLINE\n"); return BREAKLINE; }
"#" { printf("Token Identified: COMENTARIO\n"); return COMENTARIO; }
"@" { printf("Token Identified: INGREDIENTE\n"); return INGREDIENTE; }
"%" { printf("Token Identified: PASSO\n"); return PASSO; }
"(" { printf("Token Identified: LEFT PARENTHESIS\n"); return LEFT_PARENTHESIS; }
")" { printf("Token Identified: RIGHT PARENTHESIS\n"); return RIGHT_PARENTHESIS; }
"," { printf("Token Identified: COMMA\n"); return COMMA; }
"PRE-AQUECER-FORNO" { printf("Token Identified: PRE-AQUECER-FORNO\n"); return PRE_AQUECER_FORNO; }
"MISTURAR" { printf("Token Identified: MISTURAR\n"); return MISTURAR; }
"ADICIONAR" { printf("Token Identified: ADICIONAR\n"); return ADICIONAR; }
"MISTURAR-POR" { printf("Token Identified: MISTURAR-POR\n"); return MISTURAR_POR; }
"ASSAR" { printf("Token Identified: ASSAR\n"); return ASSAR; }
"xicara"|"colher_cha"|"colher_sopa" { printf("Token Identified: UNIDADE\n"); return UNIDADE; }

{DIGIT}+ { printf("Token Identified: NUMBER\n"); return NUMBER; }
\"(\\.|[^\"\n])*\" { printf("Token Identified: STRING\n"); return STRING; }
[a-zA-Z_][_a-zA-Z0-9]* { printf("Token Identified: WORD\n"); return WORD; }

.  { printf("Unknown token: %s (ASCII: %d)\n", yytext, (int)yytext[0]); yyterminate(); };

%%