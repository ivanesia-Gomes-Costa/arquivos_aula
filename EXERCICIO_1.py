nome = input('Qual o nome do Aluno? ')
nota = int(input('Qual a nota do Aluno? '))

if (nota >= 0 and nota < 3):
    conceito = 'E'
    print("O aluno ", nome, " tirou nota ", nota, " e se enquandra no conceito E")

elif (nota >= 3 and nota < 5):
    conceito = 'D'
    print("O aluno ", nome, " tirou nota ", nota, " e se enquandra no conceito D")

elif (nota >= 5 and nota < 7):
    conceito = 'C'
    print("O aluno ", nome, " tirou nota ", nota, " e se enquandra no conceito C")

elif (nota >= 7 and nota < 9):
    conceito = 'B'
    print("O aluno ", nome, " tirou nota ", nota, " e se enquandra no conceito B")

elif (nota >= 9 and nota <= 10):
    conceito = 'A'
    print("O aluno ", nome, " tirou nota ", nota, " e se enquandra no conceito A")

else:
    print('nota invalida')






