from os import system as limpar
limpar("cls")

# #for com  um parâmetro conta de 1 em 1 até o valor do parâmetro
# for x in range (10):
#     print(f"Valor de x: {x}")

# #for com dois parâmetros inicia a variavél no valor 
# #do primeiro parâmetro e conta de 1 em 1
# #até o valor do segundo parâmetro
# for x in range (5,10):
#     print(f"Valor de x: {x}")

# #for com três parâmetros inicia a variável no valor
# #do primeiro parâmetro em saltos de valor do
# #terceiro parâmetro
# #até o valor do segundo parâmetro
# for x in range (10,0,-1):
#     print(f"Valor de x: {x}")

# for numero in range (100 + 1):
#     if numero % 10 == 0:
#         print(numero)

# value = int(input("Digite um valor:\n "))

# for i in range (value + 1):
#     if i % 10 == 0 and i > 0:
#         print(i)

# for i in range (51):
#     if i >= 0:
#         print(i)


# for i in range (51):
#     print(i, end= " ")        

# nome = input("Digite seu nome: ")

# for i in nome:
#     print(i, end= " ")

# nome = input("Digite seu nome: ")
# vogais = "aeiouAEIOU"

# for i in nome:
#     if i not in vogais:
#         print(i, end= " ")

print("Sistema Inteligente")
frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0

for i in frase:
    print(i)

    if i in vogais:
        contador += 1
        print(i)




