import os
clear = lambda: os.system("cls")
clear()

peso = float(input("Cuanto pesa?: "))

print("  ")

altura = float(input("Cuanto mides?: "))

IndiceIMC = int(peso / float(altura * float(altura )))

print("   ")

print("Su IMC es: ", IndiceIMC)

if( IndiceIMC < 18.5):
    print("Usted tiene bajo peso")
elif( IndiceIMC >= 18.5 and peso <= 24.9):
    print("Usted tiene un peso normal")
elif( IndiceIMC >= 25.0 and peso <= 30.0):
    print("Usted tiene sobrepeso")
else :
    print("Usted tiene sobrepeso")


