# - Acesso a conta com condicionais
dados = {
    'login':[],
    'senha':[]
}

print('Cadastrs-se')

cad_login = input('cadastese seu login: ')

cad_senha = input('cadastrase sua senha: ')

dados['login'].append(cad_login) 

dados['senha'].append(cad_senha
)

print()

# - 3 chances de acessar o sistema
c = 3
while c > 0 and c<4:
    c = c - 1
    print('acesse a aplicação')
    
    print()

    acesso_login = input('digite seu login para acessar: ')
    acesso_senha = input('digite sua senha para acessar: ')

    print()

    if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]:

       print('Seja bem vindo ao sistema de média')
       c=9
       
       # - Inserir notas (se Senha correta)
       print()
       aluno = input('Qual o nome do aluno ')
       print()
       n1=int(input('Digite uma nota '))
       n2=int(input('Digite uma nota '))
       n3=int(input('Digite uma nota '))
       n4=int(input('Digite uma nota '))

       # - Fazer a média
       media= (n1 + n2 + n3 + n4) / 4
       print('Aluno- ',aluno,'tem a média de- ', media)

       print()

  # - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)     
if c==9:
    print('Você acessou a média das notas')

else:
    print('Você errou as 3 vezes então sua conta será bloqueada')  


