#criando a função


#ex 1


def mostre_um_texto():#criando a função

    print('texto')


mostre_um_texto()#invocando a função


#ex 2
def soma():
  n1 = float(input('n1: '))
  n2 = float(input('n2: '))

  print('= ',n1+n2)

def sub():
  n1 = float(input('n1: '))
  n2 = float(input('n2: '))

  print('= ',n1-n2) 

def multi():
  n1 = float(input('n1: '))
  n2 = float(input('n2: '))

  print('= ',n1*n2)

def div():
  n1 = float(input('n1: '))
  n2 = float(input('n2: '))

  print('= ',n1/n2)

def calculadora():
    operacao=input('''

    escolha a operação:

                +

                -

                /

                *
    ''')

    if operacao == '+':
      soma()

    elif operacao == '-':

      sub()

    elif operacao == '/':

      div()

    elif operacao == '*':

      multi()

    else:

      print('Digite algo valido')
def loop():

 while True:
        calculadora()

loop()