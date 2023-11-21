# Cook Language

### Descrição
_______________________________
Linguagem de programação desenvolvida para a disciplina de Lógica da Computação do curso de Engenharia de Computação do Insper. A linguagem foi desenvolvida para para ler e interpretar receitas de culinária como instruções para um robô de cozinha.

### Desenvolvido por
___________________________
Sarah Pimenta

### EBNF:
_______________________________
para o robô, facilitando a automação do processo de cozimento.
```
RECIPE = HEADER, BREAKLINE, INGREDIENT_LIST, BREAKLINE, STEP_LIST;

HEADER = COMENTARIO, SPACE, TITLE_LINE;

TITLE_LINE = TITLE, {SPACE, TITLE};

TITLE = WORD;

INGREDIENT_LIST = INGREDIENT, {BREAKLINE, INGREDIENT};

INGREDIENT = INGREDIENTE, SPACE, WORD, SPACE, NUMBER, SPACE, UNIDADE;

STEP_LIST = {STEP_LIST, BREAKLINE, STEP};

STEP = PASSO, SPACE, ACTION;

ACTION = PRE_AQUECER_FORNO, LEFT_PARENTHESIS, NUMBER, COMMA, NUMBER, RIGHT_PARENTHESIS
       | MISTURAR, LEFT_PARENTHESIS, INGREDIENTS, RIGHT_PARENTHESIS
       | ADICIONAR, LEFT_PARENTHESIS, INGREDIENTS, RIGHT_PARENTHESIS
       | ASSAR, LEFT_PARENTHESIS, NUMBER, COMMA, NUMBER, RIGHT_PARENTHESIS;

INGREDIENTS = WORD, {COMMA, [SPACE], WORD};
```

### Exemplo de Programa
___________________________________
```
# Bolo de Chocolate
@ farinha 2 xicara
@ acucar 1 xicara
@ manteiga 1 coler_cha

% PRE-AQUECER-FORNO(250,15)
% MISTURAR(farinha, manteiga, acucar)
```
### Flex e Bison
____________________________
Para fazer a análise sintática e léxica da linguagem, foram utilizados o Flex e o Bison.

Para compilar o programa, é necessário ter o Flex e o Bison instalados. Assim, para fazer as análises, basta rodar os seguintes comandos no terminal:


```
cd Flex_Bison
flex -l cook.l
bison -dv parser.y
gcc -o analyzer parser.tab.c lex.yy.c -lfl
./analyzer < receita.txt
```
