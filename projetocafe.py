# Menu = "************************"
# Menu2 = "*** CAFÉ's SENAI *******"
# Cardapio = "ESCOLHA UMA BEBEIDA ABAIXO:"
# opção1 = "1-CAFÉ EXPRESSO"
# opção2 = "2-CAFÉ COM LEITE"
# opção3 = "3-CAPPUCCINO"
# opção4 = "4-ÁGUA QUENTE"
# opção5 = "5-LEITE PURO"
# print(Menu)
# print(Menu)
# print(Menu2)
# print(Menu)
# print(Cardapio)
# print(opção1)
# print(opção2)
# print(opção3)
# print(opção4)
# print(opção5)
# print(Menu)

# print(Menu, "\n", Menu, "\n", Menu2, "\n", Menu, "\n", Cardapio, "\n", opção1, "\n", opção2,"\n", opção3, "\n", opção4, "\n", opção5, "\n", Menu)

from os import system as limp
from time import sleep as Tempo
limp("cls")

print(("*" * 43 + "\n") * 3)
print("*" * 10, end="")
print("\tCAFÉ's SENAI\t","*" * 10)
print("*" * 43)
print("ESCOLHA UMA BEBIDA ABAIXO: \n\n1 - CAFÉ EXPRESSO\n\
2 - CAFÉ COM LEITE\n3 - CAPPUCCINO\n4 - ÁGUA QUENTE\
\n5 - LEITE PURO")
print("\u2764\ufe0f\u200d * 20")
print("*" * 43, "\n\n")

opção = int(input("Escolha uma opção: "))
if opção == 1:
    print("Você selecionou CAFÉ EXPRESSO")
    print("Fazendo o seu café", end="")
    for i in range (10):
        Tempo (1)
        print(".", end="")
elif opção == 2:
    print("Você selecionou CAFÉ COM LEITE")
elif opção == 3:
    print("Você selecionou CAPPUCCINO")
elif opção == 4:
    print("Você selecionou ÁGUA QUENTE")
elif opção == 5:
    print("Você selecionou LEITE PURO")
else:
    print("ERRO, ESCOLHA UMA OPÇÃO VÁLIDA")


    