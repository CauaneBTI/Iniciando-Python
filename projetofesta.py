from os import system as limpar
limpar("cls")

print("********Bem vindo a festa do Senai***********")
ano = int(input("Insira o ano em que nasceu"))
idade = 2025 - ano
limpar("cls")
if idade >= 18:
    print("Pode entrar na festa, bem vindo")
else:
    print("Não pode entrar, bye")

