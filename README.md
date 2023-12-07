# Cook Language
_______________________________
### Descrição

Linguagem de programação desenvolvida para a disciplina de Lógica da Computação do curso de Engenharia de Computação do Insper. A linguagem foi desenvolvida para para ler e interpretar receitas de culinária como instruções para um robô de cozinha.

### Desenvolvido por

Sarah Pimenta
___________________________
### EBNF:

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
_______________________________
### Exemplo de Programa

```
# Bolo de Chocolate
@ farinha 2 xicara
@ acucar 1 xicara
@ manteiga 1 coler_cha

% PRE-AQUECER-FORNO(250,15)
% MISTURAR(farinha, manteiga, acucar)
```
___________________________________
### Flex e Bison

Para fazer a análise sintática e léxica da linguagem, foram utilizados o Flex e o Bison.

Para compilar o programa, é necessário ter o Flex e o Bison instalados. Assim, para fazer as análises, basta rodar os seguintes comandos no terminal:


```
cd Flex_Bison
flex -l cook.l
bison -dv parser.y
gcc -o analyzer parser.tab.c lex.yy.c -lfl
./analyzer < ../receita.txt
```
___________________________________
### Compilador

O compilador da COOK Language utiliza como base o compilador desenvolvido na disciplina para GO. Ele faz todas as etapas de análise (léxica, sintática e semântica) e simula o preparo da receita no terminal.

Para compilar o programa de testes é necessário ter o python instalado. Para rodar, utilize o senguinte comando no terminal:

```
python compilador.py receita.txt
```
___________________________________
### Apresentação

A apresentação da linguagem está disponível em pdf no arquivo COOKLanguagePresentation.pdf
