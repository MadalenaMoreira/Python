ana = 0
bruno = 0
carla = 0

print("1 - Ana")
print("2 - Bruno")
print("3 - Carla")

while True:
    voto = int(input("Insira o seu voto: "))
    if voto == 1:
        ana = ana + 1
    elif voto == 2:
        bruno = bruno + 1
    elif voto == 3:
        carla = carla + 1
    else:
        break

print(f"A Ana teve {ana} votos")
print(f"O Bruno teve {bruno} votos")
print(f"A Carla teve {carla} votos")

if ana > bruno and ana > carla:
    print("A Ana foi a mais votada. ")
if bruno > ana and bruno > carla:
    print("O Bruno foi o mais votado. ")
if carla > ana and carla > bruno:
    print("A Carla foi a mais votada. ")
