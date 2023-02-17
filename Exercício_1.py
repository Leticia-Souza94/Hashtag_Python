codigo_produto = input("Digite o código do produto: ").upper()

if ("BAC" in codigo_produto):
    print("O produto é alcoolico")
elif ("BEB" in codigo_produto):
    print("O produto não é alcoolico")

else:
    print("Código Inválido!")