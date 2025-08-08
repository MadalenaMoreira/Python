altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso. ")

elif 25 <= imc < 30:
    print("Sobrepeso. ")

else:
    print("Peso normal. ")