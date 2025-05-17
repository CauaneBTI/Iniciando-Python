from os import system as limp
limp("cls") 

# nome = "Cauane Neves dos Santos"
# print(nome)
# print("C", "\n", "A", "\n", "U", "\n", "A", "\n", "N", "\n", "E", sep="")
# for i in range(len(nome)):
#     print(nome[i])
#     print("C", "\n", "", "A", "\n" "   ", "U", "\n", "    ", "A",)

# nome = input("Insira o seu nome: \n")
# print(nome)

# data = int(input("Insira o ano em que você nasceu: \n"))
# idade = 2025 - data
# print("Sua idade é:",idade, "anos")

# nome = input("Insira o seu nome: \n")
# data_nascimento = input("Insira sua data: \n")
# CPF = int(input("Insira seu CPF: \n"))
# telefone = int(input("Insira o seu telefone: \n"))
# limp("cls") 
# print("SEUS DADOS SÃO:", "\n", "Nome:", nome, "\n", "Data de nascimento:", data_nascimento, "\n", "CPF:", CPF, "\n", "Telefone:", telefone, sep="")
# input("\nPressione Enter para continuar...")

nome = input("Insira seu nome: \n")
dia_de_nascimento = int(input("Insira o dia em que nasceu: \n"))
mes_de_nascimento = int(input("Insira o mês em que nasceu: \n"))
ano_de_nascimento = int(input("Insira o ano em que nasceu: \n"))
limp("cls")
# print("Bem Vindo", nome, "ao SENAI!!!")
# print("Sua data de nascimento é:", end="")
# print(dia_de_nascimento, mes_de_nascimento, ano_de_nascimento, sep="/")

# print(f"Bem vindo {nome} ao SENAI!!!", end="")
# print(f"\nsua data de nascimento é {dia_de_nascimento}/{mes_de_nascimento}/{ano_de_nascimento}.")

print("Bem vindo", nome, "ao SENAI!!!", "\nSua data de nascimento é:",end="")
print(dia_de_nascimento,mes_de_nascimento,ano_de_nascimento,sep="/",end=".")