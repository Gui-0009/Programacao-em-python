#Estruturas de fluxo de controle:
#palavra_reservada condição = v or f


#condicionais

nome = input('digite seu nome: ')

print()
#utilização do pass
# if nome == 'fernando':
#     pass # não ira fazer nada, no local aonde estiver

if nome == 'Caio':
        print('Seja bem vindo', nome)

if nome == 'Lucas':
     print('Você não poderá entrar...', nome)

print()
#Condicional composta if else

if nome == 'Caio':
        print('Seja bem vindo', nome)

else:
     print(nome, 
     'você não poderá entrar...')

print()
#condicional composta if elif else

if nome == 'Kaio':
    print('Seja bem vindo', nome)
elif nome == 'Lucas' and 'Lukas':
    print(nome, 'Não pode acesar')
else:
    print('Faça o cadastro')
