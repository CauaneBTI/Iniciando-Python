from os import system as limp
limp("cls")

print("Bem vindo ao sistema de informações do programa.")
print("Por favor, insira seus dados abaixo:")
nome = input("Digite seu nome: ")
dt_nasc = input("Digite seu data de nascimento: ")
cpf = int(input("Digite seu CPF: "))
tel = int(input("Digite seu telefone: "))
info = (nome, dt_nasc, cpf, tel)
print(f"\nSeus dados são:\nNome: {info[0]}\nData de Nascimento: {info[1]}\nCPF: {info[2]}\nTelefone: {info[3]}")

