import random
# Exercícios com funções:
# variáveis locais, globais e parâmetros
# 1
# CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def comparacao(n1,n2):
    d1 = n1 % 2
    d2 = n2 % 2
    if d1 != 0:
        print('Esse numero é impar')
    else:
        print('Esse numero é par')

    if d2 != 0:
        print('Esse numero é impar')
    else:
        print('Esse numero é par')
comparacao(4,9)

print()

# 2
# CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

def multiplo(n3,n4,n5):

    m = n3*n4*n5
    print('A multiplicação dos numeros é', m)
multiplo(10,10,10)

print()

# 3
# CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

def potencia(n6,n7):
    p = n6 ** n7
    print('A potencia dos numeros é',p)
potencia(2,9)

print()

# 4
# CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.

def idade(idade1):
    if idade1 == 18:
        print('Você tem 18 anos')
    else:
        print('Você não tem 18 ano')
idade(17)

print()

# 5
# DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

def sorteio(n8):
    di = random.randint(0,100)
    if n8 == di:
        print('Acertou, parabens')
    else:
        print('Você errou')
sorteio(35)

print()

# 6
# DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

def brasil(b_ganhou,ano):
    if b_ganhou == 's' and ano == 1999 or b_ganhou == 'Sim' and ano == 1999:
        print('O Brasil ganhou a copa do mundo de 1999')
    else:
        print('O Brasil perdeu a copa do mundo de 1999')

brasil('s',1999)

print()

# 7
# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
def coumprimento_restaurante(nome, sobre_nome):
    # 1 - Função - cumprimentar o cliente
    print('Sejá bem vindo', nome, sobre_nome)
def funcao_restaurante(pedido):
    # 2 - Função - restaurante

    ordem_pedido = []

    print('\nDigite seu pedido de acordo os numero.Parar de escolher(0).')

    print('\nNossas opções são:\n\nSALADA;\nMACARRONADA;\nSANDUICHE;\nSORVETE\n')

    for i in range(pedido):
        lista = input('Qual seu pedido?')
        ordem_pedido.append(lista)
    print('Seus pedidos foram:', ordem_pedido)
coumprimento_restaurante('Julios','Ferreira')
funcao_restaurante(4)
# 3 - Sugestão utilize listas e loops