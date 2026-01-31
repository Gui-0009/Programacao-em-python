print('Sistema de notas')
print('-' * 32)
print()
nome_aluno = input('nome do aluno: ')
print()
n1_port = float(input('Nota Portugues: '))
n2_mat = float(input('Nota Matemarica: '))
n3_ing = float(input('nota Ingles: '))
print()
media = (n1_port +n2_mat + n3_ing)/3
print('Média do', nome_aluno,':')
print()
aprovado = media >=7
reprovado = media <5
recuperação = media >=5 and media <7
print()
print('Aprovado?', aprovado)
print('reprovado', reprovado)
print('recuperação', recuperação)
