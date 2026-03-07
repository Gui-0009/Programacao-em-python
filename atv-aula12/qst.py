# **1 - Crie um número aleatório de 5,10**

import random

def atv1(n1,n2):
    return random.randint(n1,n2)



# **2 - Crie 3 números aleatórios**

def atv2(x,y):
    return random.randint(x,y)


# **3 - Crie um número aleatório entre 10 a 30 utilize o range()**

def atv3(x,y):
    return random.randint(x,y)




# **4 - Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)

def atv4(x):

    for i in range(x,0,-1):
        print(i)

    print('fogo')


# **5 - Soma de números pares**

# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

# ```python
def atv5(n_int1,f):
# # Peça ao usuário que insira um número inteiro 
   if n_int1 > 0: 
# # faça o loop com range e for ate´o numero
# # positivo e, em seguida, calcule a soma de 
        for i in range(0,n_int1,2):
            f += i
        print(f)
# # todos os números pares de 2 até o número inserido.
# ```

# (use módulo, if, for)




# **6 - Tabuada de multiplicação**

def atv6(num1):
# ***Utilize print() na saída***

# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
    for i in range(10):
        print(num1*i)
# (while ou for )

# **7 -  Números ímpares reversos**
def atv7(x,y):
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
    for i in range(x,y,-2):
        print(i)
    
# (for)

# ***Chamar todas elas para o arquivo main()***