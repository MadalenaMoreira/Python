kwh = int(input("Qual a quantidade de kwh consumida? "))
tipo = input("Qual o tipo de instalação? ")

if tipo == "R":
    if kwh <500:
        print(f"O preço será de {kwh * 0.40}")
    else:
        print(f"O preço será de {kwh * 0.65}")
if tipo == "C":
    if kwh <1000:
        print(f"O preço será de {kwh * 0.55}")
    else:
        print(f"O preço será de {kwh * 0.60}")
if tipo == "I":
    if kwh <5000:
        print(f"O preço será de {kwh * 0.55}")
    else:
        print(f"O preço será de {kwh * 0.60}")