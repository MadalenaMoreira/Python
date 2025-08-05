velocidade = int(input("Qual a velocidade a que o veículo passou? "))

if velocidade > 80:
    x = velocidade - 80
    multa = x * 2
    print(f"Estás acima do limite permitido. A multa foi gerada no valor de {multa} euros")
if velocidade <= 80:
    print("Dentro do limite. Boa viagem!")