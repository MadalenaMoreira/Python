salario = int(input("Qual o ordenado atual? "))

if salario < 500:
    print(f"O novo salario do funcionario passará para {salario + (salario * 0.15)}")
elif salario <1000:
    print(f"O novo salario do funcionario passará para {salario + (salario * 0.10)}")
else:
    print(f"O novo salario do funcionário passará para {salario + (salario * 0.05)} ")