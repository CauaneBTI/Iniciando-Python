
from os import system as limpar
limpar("cls")

# Entrada de dados
pressao = float(input("Digite sua pressao: "))
temperatura = float(input("Digite sua temperatura: "))
bpm = int(input("Digite seus batimentos cardiacos: "))

# Avaliação da Pressão
if pressao >= 10.1 and pressao <= 14:
    status_pressao = "Normal"
    print("Sua pressão está Normal")
elif pressao > 14.1:
    status_pressao = "Alta"
    print("Sua pressão está Alta")
else:
    status_pressao = "Baixa"
    print("Sua pressão está Baixa")

# Avaliação da Temperatura Corporal
if temperatura < 35:
    status_temperatura = "Hipotermia"
    print("Sua temperatura está abaixo de 35°C - Hipotermia")
elif 35.5 <= temperatura <= 37.5:
    status_temperatura = "Normal"
    print("Sua temperatura está entre 35.5°C e 37.5°C - Normal")
elif 37.6 <= temperatura <= 38.9:
    status_temperatura = "Febre Leve"
    print("Sua temperatura está entre 37.6°C e 38.9°C - Febre Leve")
else:
    status_temperatura = "Febre Alta"
    print("Sua temperatura está acima de 38.9°C - Febre Alta")

# Avaliação dos Batimentos Cardíacos
if bpm > 100:
    status_bpm = "Taquicardia"
    print("Seus batimentos estão acima de 100 bpm - Taquicardia")
elif bpm < 60:
    status_bpm = "Bradicardia"
    print("Seus batimentos estão abaixo de 60 bpm - Bradicardia")
else:
    status_bpm = "Normal"
    print("Seus batimentos estão entre 60 e 100 bpm - Normal")

# Classificação final
print("\n--- Classificação do Caso ---")
if status_temperatura in ["Normal", "Febre Leve"] and status_bpm == "Normal" and status_pressao == "Normal":
    print("Classificação: CASO DE ATENDIMENTO NORMAL")
elif status_temperatura == "Febre Alta" and status_bpm == "Taquicardia" and status_pressao == "Alta":
    print("Classificação: CASO DE ATENDIMENTO GRAVE")
elif status_temperatura == "Hipotermia" and status_bpm == "Bradicardia" and status_pressao == "Baixa":
    print("Classificação: CASO DE ATENDIMENTO URGENTE")
else:
    print("Classificação: CASO INDETERMINADO - Consulte um médico")
