from os import system as limpar
limpar("cls")

numero = float(input("Digite um numero: "))
if numero > 0:
    print("o numero é positivo")
if numero == 0:
    print("Zero")
if numero < 0:
    print("Negativo")

if valor > 0:
    print("O numero é positivo")
elif valor < 0:
    print("O numero é negativo")
elif valor == 0:
    print("O numero é zero")

numero = float(input("Digite um numero: "))
if numero == 0:
    print("O numero é zero")
if numero > 0:
    print("O numero é positivo")
else:
    print("O numero é negativo")

print("__________Bem vindo ao sistema__________")
senha = input("Digite a senha: ")
limpar("cls")
if senha == "Python123":
    print("Acesso permitido")
else:
    print("Senha incorreta, você não é o usuario master")



