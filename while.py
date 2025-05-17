from os import system as limpar
limpar("cls")

# pessoas = 10

# while pessoas > 0:
#     print(f"Contagem de pessoas: {pessoas}")
#     pessoas -=1


# print("********Bem vindo ao Sistema***********")
# # senha = input("Digite a senha para desbloquear: ")

# # while senha == "comando":
# #     print("SENAI NA VEIA 🍒")

# # while senha != "comando":
# #     print("Digite a senha correta")

# passaword = "cerejinha"
# senha = None

# while passaword != senha:
#     senha = input("Digite sua senha:\n")
# print("Acesso concedido, bem vindo ao sistema Cereja 🍒"

# contador = 1
# numero = int(input("Digite um numero:\n"))

# while contador <= 10:
#     print(numero, "*", contador, "=", numero * contador)
#     contador = contador + 1

while True:
    numero = int(input("\n\nDigite um número para a tabuada:\n"))
    x = 1
    print("Sistema de tabuada SENAI")
    while x <=10:
        print(f"{x} * {numero} = {x * numero}")
        x += 1
    if numero == 1000:
        break

pares = 0

while pares < 3:
    numero = int(input("Digite um número inteiro:\n"))
    if numero % 2 == 0:
        print("O número é PAR.")
        pares += 1
    else:
        print("O número é ÍMPAR.")
        
print("Obrigado!")





