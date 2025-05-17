from os import system as limpar
limpar("cls")

pressao = float(input("Digite sua pressao: "))
temperatura = float(input("Digite sua temperatura: "))
bpm = int(input("Digite seus batimentos cardiacos: "))

#Pressao
normal = "Entre 10.1 e 14"
alta = "Maior que 14.1"
baixa = "Menor que 10.1"

if pressao >=10.1 and pressao <=14.1: print("sua pressao está", normal)
if pressao >14.1: print("Sua pressao está", alta)
if pressao <10.1: print("Sua pressao está", baixa)

#Temperatura corporal
hip = "Abaixo de 35°C"
normal = "Entre 35.5°C e 37.5°C "
Feb_leve = "De 37.6°C a 38.9°C"
Feb_alta = "Acima de 38.9°C"

if temperatura <35: print("sua temperatura está", hip)
if temperatura >=35.5 and temperatura <=37.5: print("Sua temperatura está", normal)
if temperatura >=37.6 and temperatura <=38.9: print("Sua temperatura está", Feb_leve)
if temperatura >38.9: print("Sua temperatura está", Feb_alta)

#BPM
Taquicardia = "Acima de 100 bpm"
Bradicardia = "Abaixo de 60 bpm"
Normal = "Entre 60 e 100 bpm"

if bpm >100: print("Seus batimentos estão em", Taquicardia)
if bpm <60: print("Seus batimentos estão em", Bradicardia)
if bpm >=60 and bpm <=100: print("Seus batimentos estão", Normal)