import random

numero = int(input("Insira um número entre 0 e 5: "))

numero_aleatorio = random.randint(0,5)
print(numero_aleatorio)

if numero == numero_aleatorio:
    print("Parabéns! Você acertou")

else:
    print("Você errou. Tente novamente.")