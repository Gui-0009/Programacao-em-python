idade = 18

#Olha a condição
if idade>=18:
    print('Maior de idade')
else:
    print('Menor de idade')

#não olha a condição, match olha pra dentro da varisvel

match idade: #
    case 18: #case é tipo o if
        print('Maior de idade')
    case _:  #'case _' é tipo o else
        print('Menor de idade')
        