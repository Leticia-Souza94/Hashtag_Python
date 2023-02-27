# Curso de Python com a Hashtag Treinamentos
## Índice
[Exercício 1](https://github.com/Leticia-Souza94/Hashtag_Python/blob/main/Exerc%C3%ADcio_1.py)<br><br>
[Exercício 2](https://github.com/Leticia-Souza94/Hashtag_Python/blob/main/Exerc%C3%ADcio_2.py)<br><br>
<br>
## Exercício 1
### Enunciado do exercício:
abordagem de inputs e strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto. Ex: <br>
<br>
Coca -> Código: BEB1300543<br>
Pepsi -> Código: BEB1300545<br>
Vinho Primitivo Lucarelli -> Código: BAC1546001<br>
Vodka Smirnoff -> Código: BAC17675002<br>
<br>
Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
<br>
<br>
<br>
### Resolução do exercício:
1) Inciei escrevendo uma linha que capturasse a resposta do funcionário da Hashtag&Drink:

codigo_produto = input("Digite o código do produto: ")<br>

2) Poderia utilizar apenas a função print para mostrar se dentro do código inserido existe as inciais "BAC", mostrando a resposta True. Se não for encontrado as inciais "BAC" o sistema retornaria false:

codigo_produto = input("Digite o código do produto: ")<br>
entrada: BAC1546001<br>
print("BAC" in codigo_produto)<br>
imprime: True<br>

3) Se o usuário digitar o código da bebida em letras minúsculas o programa retornará um erro. Por isso, podemos inserir a função upper() para transformar as letras da respostas em maiúsculas:

codigo_produto = input("Digite o código do produto: ").upper()<br>

4) Podemos tambem inserir a função if e else para retornar as respostas "O produto é alcoolico" e "O produto não é alcoolico". Caso o código não possua as iniciais "BEB" e "BAC", poderá retornar a resposta "Código Inválido!".

codigo_produto = input("Digite o código do produto: ").upper()

if ("BAC" in codigo_produto):<br>
    print("O produto é alcoolico")<br>
elif ("BEB" in codigo_produto):<br>
    print("O produto não é alcoolico")<br>

else:<br>
    print("Código Inválido!")<br>

[Clique Aqui para acessar o código desse exercício](https://github.com/Leticia-Souza94/Hashtag_Python/blob/main/Exerc%C3%ADcio_1.py)
<br>
<br>
<br>
<br>
## Exercício 2
### Enunciado do exercício:
abordagem sobre if e else

Digamos que você precisa criar um programa para um fundo de investimentos conseguir avaliar o resultado de uma carteira de ações e o quanto de taxa deverá ser pago.<br><br>

- O fundo se compromete a entregar no mínimo 5% de retorno ao ano.<br>
- Caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores.<br>
- Caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa dos seus investidores.<br>
- Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores.<br>
<br>
<br>
### Resolução do exercício:

1) Inciei escrevendo uma linha que capturasse a resposta sobre o valor investido:

investimento = float(input("Digite o valor investido: "))

2) Criei variáveis para meta, taxa e retorno:

meta = 0.05
taxa = 0
retorno = 0.04

3) Calculei o valor investido * o retorno e somei o resultado ao valor investido, assim conseguimos saber o valor total após o retorno (sem descontar as taxas):

investimento_retorno = (investimento * retorno) + investimento
print(f"O valor total após o retorno sem a cobrança das taxas é de R$ {investimento_retorno}")

4) Trabalhei com if e else para adicionar as condições. Podem ser cobradas taxas de 2%, 4% ou nenhuma taxa, seguindo as condições do enunciado:

if (retorno > meta):<br>
    if (retorno > 0.20):<br>
        taxa = 0.04<br>
        print(f"Será cobrado uma taxa de 4% sobre o rendimento. Total de R${(investimento * retorno) * taxa}")<br>
    else:<br>
        taxa = 0.02<br>
        print(f"Será cobrado uma taxa de 2% sobre o rendimento. Total de R${(investimento * retorno) * taxa}")<br>
else:<br>
    taxa = 0<br>
    print("Não será cobrado uma taxa!")<br>
    
[Clique Aqui para acessar o código desse exercício](https://github.com/Leticia-Souza94/Hashtag_Python/blob/main/Exerc%C3%ADcio_2.py)
<br>
<br>
<br>
