import random

#adicionha um numero aleatorio na variavel 'aleatorio'
aleatorio = random.randint(1.10)
#Muda a varavel 'chute' de acordo o que sera escrido pelo jogador e o transformara em um numero ineiro.
chute = int(input('chute um numero'))

#se numero a variael 'aleatorio' for igual ao numero na variavel 'chute'
if aleatorio == chute:
     #se sim, então mostra o resultado possitivo
     print('acertei em cheio')
     #irá mostrar o numero da variavel 'aleatoria'
     print('o numero é ', aleatorio)
else:
     #se não, então mostra o resultado negativo
     print('errou feio')    
      #irá mostrar o numero da variavel 'aleatoria'
     print('o numero é ', aleatorio)

