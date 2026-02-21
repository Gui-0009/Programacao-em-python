#atv 1

numero = int(input('numero: '))
match numero:
    case x if numero %2 ==0:
        print('par-')
    case _:
        print('impar-')

print()

#atv 2

n = int(input('Digite um numero: '))
match n:
    case x if n > 0:
        print('Esse numero é positivo')
    case x if n==0:
        print('Esse numero é igual a zero')
    case _:
        print('Esse numero é negativo')

print()

#atv 3

minha_sting = ""

texto = input("Digite algo")
match texto:
    case "":
        print("A string está vazia")
    case _:
        print("A string não está vazia")
print()

#atv 4 

n3 = int(input('Diga um numero '))

match n3:
    case x if n3<10:
        print('Menor que 10')
    case x if n3>10:
        print('Maior que 10')
    case _:
        print('Numero é 10')

print()

#atv 5

idade = int(input('Qual sua idade? '))

match idade:
    case x if idade <=12:
        print('Criança')

    case x if idade <=17 and idade>12:
        print('Adolescente')

    case x if idade <=35 and idade>17:
        print('Jovem')

    case x if idade<35 and idade>64:
        print('Adulto')
    case _:
        print('Idoso')
