from os import system as limp
limp("cls")

# #para criar dicionário
info = {"Nome":"Cauane","DataNasc":"09/12/2002","CPF":"12345678912"}
# print(info["Nome"])

# #editar valor de dicionário
# info["Nome"] = "Cah"
# print(info)

# #inserir novo valor de dicionário
# info["Nome"] = "Senai"
# print(info)


# #para deletar item o dicionario
# del(info["Nome"])
# print(info)

# nome = input("Digite seu nome: ")
# dt_nasc = input("Digite seu data de nascimento: ")
# cpf = int(input("Digite seu cpf: "))
# tel = int(input("Digite seu telefone: "))

# info = {"nome": nome,"data_nascimento": dt_nasc,"cpf": cpf,"telefone": tel}

# info = {"nome": input("Digite seu nome: "),"data_nascimento": input("Digite sua data de nascimento: "),"cpf": input("Digite seu CPF: "),"telefone": input("Digite seu telefone: ")}
# print(f"\nSeus dados são:\nNome: {info['nome']}\nData de Nascimento: {info['data_nascimento']}\nCPF: {info['cpf']}\nTelefone: {info['telefone']}") 

print("Seja bem vindo ao bday Caah💕")
convidados = []

while len(convidados) < 30:
    nome = input("Digite seu nome: ")
    if nome == "100":
        for i in convidados:
            print("Lista encerrada")
        break
    convidados.append(nome)
    print(f"{nome} foi adicionado à lista. ({len(convidados)}/30)")
print("\nA festa começou! 🎉 Lista de convidados que vieram:")
for i in range(len(convidados)):
    print(f"Convidados{i}: {convidados[i]}")

    









