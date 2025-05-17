from os import system as limp
limp("cls") 

# valor1 = 5
# valor2 = 3

valor1 = int(input("\nDigite um valor"))
valor2 = int(input("\nDigite um valor"))

# valor1 = float(input("Digite um valor"))
# valor2 = float(input("Digite um valor"))

soma = sub = mult = div = exp = None

# soma = None
# sub = None
# mult = None
# div = None
# exp = None

soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
div = valor1 / valor2
exp = valor1 ** valor2

print("Valor da soma:", soma)
print("Valor da subtração:", sub)
print("Valor da multiplicação:", mult)
print("Valor da divisão:", div)
print("Valor da exponenciação:", exp)