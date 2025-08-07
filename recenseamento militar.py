from datetime import date

ano_nascimento = int(input("Insira a sua data de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print("Ainda não tens idade para o recenseamento.")

elif idade > 25:
    print("Já passou o prazo para o recenseamento.")

else:
    print("Está no momento para o recenseamento.")