# 1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.


t = 0


while t<1001:
    print(t)
    t = t+1

# 2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

lista_nome = []
quantidade = 10
for n in range(10):
    nome = input('Digite um nome ')
    lista_nome.append(nome)
else:
    print('Nomes: ', lista_nome)