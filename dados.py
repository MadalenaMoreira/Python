import random

dado1 = 1
dado2 = 2
contagem = 0

while dado1 != dado2:
    dado1 = random.randint (1, 6)
    dado2 = random.randint  (1, 6)
    contagem = contagem + 1


print(f"Precisaste de {contagem} jogadas! ")
