
print('Exercício 1:')
print()

# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

def atv1():
    try:
         n1 = int(input('Digite um numero'))
         print(n1)
    except ValueError:
         print('Você deve inserir o dado solicitado')
    else:
         ('Pode seguir')
    finally:
         ('Processo finalizado')

atv1()


print('Exercício 2:')

# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

def atv2():
    try:
         n2 = int(input('Digite o primeiro numero da divisão'))
         n3 = int(input('Digite o segundo numero da divisão'))
         print(n2 / n3)
    except ValueError:
         print('Digite o tipo de dado solicitado')
    except TypeError:
         print('Dado colocados não são compativeis com os solicitados')
    except ZeroDivisionError:
         print('numero não pode ser dividido por 0')
    else:
         print('Pode seguir')
    finally:
         print('Processo terminado')
atv2()

print('Exercício 3:')
print()
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).


def atv3():
    try:
         l = [1,2,3,4]
         print(l[9])
    except IndexError:
         print('Index nã oencontrado')
    except ValueError:
         print('Digite outro numero')
    else:
         print('Pode seguir em frende')
    finally:
         print('Processo acabado')
atv3()