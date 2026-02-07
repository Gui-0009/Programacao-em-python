# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input('digite um numero :'))

if numero >0:
    print('positivo')
#elif numero <0:
    print('negativo')
else:
    print(0)

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('digite sua idade'))
n=16
if idade >=n:
     print('Você pode votar')
     print('Você não pode votar')
# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
import random

n = random.randint (0,70)
print(n)

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.


# 5*
# Determine se um número é múltiplo de 5 e 7.
import random

n = random.randint (0,70)
print(n)
n1=n%5
n2=n%7
print('resto de ',n, 'é ',n1)
print('resto de ',n, 'é ',n2)
if n%5 and n%7:
    print('N é um número multiplo de 5 e 7')
else:
     print('N não é um número multiplo de 5 e 7')

# 6*
# Verifique se um número é positivo e maior que 10
import random

n = random.randint (-70,70)
print(n)
if n>0 and n>10:
     print('verdadeiro')
else:
    print('falso')

# 7*
# Verifique se um número é divisível por 3 ou 5.
import random

n = random.randint (0,50)
print(n)
n1=n%3
n2=n%5
print(n1)
print(n2)
if n%3 or n%5:
          print('verdadeiro')
else:
    print('falso')