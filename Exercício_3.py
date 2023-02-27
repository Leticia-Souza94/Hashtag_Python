meta = 20000
bonus = 0
valor_vendido = 70000


if (valor_vendido >= meta * 2):
    bonus = 0.07
    print("Uaaaaaauuuu, você ganhou um bônus de 7% das vendas! Você vai receber R$ {:.2f}".format(valor_vendido * bonus))
elif (valor_vendido > meta):
    bonus = 0.03
    print("Parabéns, você ganhou um bônus de 3% das vendas. Você vai receber R$ {:.2f}".format(valor_vendido * bonus))
else:
    print("Você não ganhou bônus dessa vez!")