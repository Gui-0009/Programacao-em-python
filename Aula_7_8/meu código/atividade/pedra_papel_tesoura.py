#biblioteca que fará com que a maquina faça uma ação 'aleatória'.
import random
#fará com que a maquina escolha um elemento aleatório que está dentro da lista.
numero_aleatorio = random.choice
#imprima o resultado da esolha da maquina, em forma de numero.
#print(numero_aleatorio)

#Insere a 
lista_maquina = ['🪨','🧻','✂️']
#imprima o resultado da esolha da maquina, em forma de 'papel, pedra ou tesoura'.
print(lista_maquina)
#coloca na variavel 'chute_maquina' um numero, que se iguala a uma figura, que foi sorteado da variavel lista_maquina
chute_maquina = random.choice(lista_maquina)

#indice_maquina = lista_maquina.inde(lista_maquina[chute_maquina])

#mostra o chute da maquina
print(chute_maquina)
#mostra as opções do jogaor
print('Pedra Papel Tesoura')
#é a lisa das opções de jogadas
minha_lista = ['🪨','🧻','✂️']

#fala pro jogador escolher uma opção
#print('escolha seu icone')

#mostra as opções do jogador
print('0- 🪨/ 1- 🧻 / 2- ✂️')

#pede pro jogador escolher um numero que se iguala a figura.
meu_chute = int(input('escolha pelo indice:'))

#mostra a figura escolhida
#print(minha_lista[meu_chute])

#se o chute da maquina for = ao meu chute, vai dar empate
if chute_maquina == minha_lista[meu_chute]:
     print('empate')
     print('****'*10)
     print('escolha ,aquina - ', chute_maquina)
     print('minha escolha - ',minha_lista, meu_chute)
#todos as possiilidade de vitoria da maquina.
if chute_maquina == '🪨' and minha_lista[meu_chute] == '✂️':
     print('Vitoria')
     print('****'*10)
     print('escolha ,aquina - ', chute_maquina)
     print('minha escolha - ',minha_lista, meu_chute)
     
if chute_maquina == '✂️' and minha_lista[meu_chute] == '🧻':
     print('Vitoria')
     print('****'*10)
     print('escolha ,aquina - ', chute_maquina)
     print('minha escolha - ',minha_lista, meu_chute)

if chute_maquina == '🧻' and minha_lista[meu_chute] == '🪨':
     print('Vitoria')
     print('****'*10)
     print('escolha ,aquina - ', chute_maquina)
     print('minha escolha - ',minha_lista, meu_chute)

#todas as posibilidade de vitória do jogador
if minha_lista[meu_chute] == '🪨' and chute_maquina == '✂️':
      print('Vitoria')
      print('****'*10)
      print('escolha ,aquina - ', chute_maquina)
      print('minha escolha - ',minha_lista, meu_chute)
     
if minha_lista[meu_chute] == '✂️' and chute_maquina == '🧻':
      print('Vitoria')
      print('****'*10)
      print('escolha ,aquina - ', chute_maquina)
      print('minha escolha - ',minha_lista, meu_chute)

if minha_lista[meu_chute] == '🧻' and chute_maquina == '🪨':
      print('Vitoria')
      print('****'*10)
      print('escolha ,aquina - ', chute_maquina)
      print('minha escolha - ',minha_lista, meu_chute)