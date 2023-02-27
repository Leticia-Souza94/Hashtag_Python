investimento = float(input("Digite o valor investido: "))

meta = 0.05
taxa = 0
retorno = 0.04

investimento_retorno = (investimento * retorno) + investimento
print(f"O valor total após o retorno sem a cobrança das taxas é de R$ {investimento_retorno}")

if (retorno > meta):
    if (retorno > 0.20):
        taxa = 0.04
        print(f"Será cobrado uma taxa de 4% sobre o rendimento. Total de R${(investimento * retorno) * taxa}")
    else:
        taxa = 0.02
        print(f"Será cobrado uma taxa de 2% sobre o rendimento. Total de R${(investimento * retorno) * taxa}")
else:
    taxa = 0
    print("Não será cobrado uma taxa!")