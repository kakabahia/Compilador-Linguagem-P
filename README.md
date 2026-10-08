### Desenvolvimento de um compilador para uma linguagem P que possui as seguintes especificações:

A linguagem P possui as seguintes características:
• é uma linguagem de tipagem forte;
• todas as variáveis e parâmetros de funções devem possuir um tipo;
• todas as variáveis devem ser declaradas antes do uso;
• existem regras restritas para compatibilidade dos tipos;
• todas as funções começam com a palavra reservada fn;
• a função principal é definida como fn main() { ... }.

3.2. Tipos
Os tipos disponíveis são:
Tipo Descrição
int inteiro
float ponto flutuante
char caractere

Tokens disponiveis
fn FUNCTION palavra reservada
main MAIN palavra reservada
let LET palavra reservada
int INT palavra reservada
float FLOAT palavra reservada
char CHAR palavra reservada
if IF palavra reservada
else ELSE palavra reservada
while WHILE palavra reservada
println PRINTLN palavra reservada
return RETURN palavra reservada
( LBRACKET abertura de parênteses
) RBRACKET fechamento de parênteses
{ LBRACE abertura de bloco
} RBRACE fechamento de bloco
-> ARROW seta de retorno
: COLON dois-pontos
; SEMICOLON ponto e vírgula
, COMMA virgula
= ASSIGN atribuição
== EQ igualdade
!= NE diferença
> GT maior que
>= GE maior ou igual
< LT menor que
<= LE menor ou igual
+ PLUS adição
- MINUS subtração
* MULT multiplicação
/ DIV divisão
[a-zA-Z]([a-zA-Z0-9_])* ID identificador
[0-9]([0-9])* INT_CONST constante inteira
[0-9]([0-9])*.[0-9]([0-9])* FLOAT_CONST constante float
’ Σ’ CHAR_LITERAL literal de caractere
"Σ+" FMT_STRING string de formatação

Estrutura obrigatória de um Token
A estrutura do token deve possuir os seguintes campos:
-lexema: guarda o lexema (string) reconhecido;
-tipo do token: guarda o tipo do token reconhecido;
-número da linha: armazena o número da linha no código-fonte em que o
token foi reconhecido.
