# Curso de Python com a Hashtag Treinamentos
## Índice
[Exercício 1](https://github.com/Leticia-Souza94/Hashtag_Python/blob/main/Exerc%C3%ADcio_1.py)
<br>
<br>
<br>
## Exercício 1
### Enunciado do exercício:
O Exercício 1 abordava inputs e strings

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

