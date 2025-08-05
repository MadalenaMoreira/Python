nota1 = int(input("qual é a primeira nota? "))
nota2 = int(input("qual é a segunda nota? "))

media = (nota1 + nota2) / 2
if media < 50:
     print("Aluno reprovado.")
if media > 50 and media < 70:
     print("É satisfeito!")
if media >= 70:
    print("É bom!")