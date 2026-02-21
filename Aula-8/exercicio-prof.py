#mercado

#dicionarios
#lista
#variaveis
#condicionas

#cadastro no e-commerce
dados = { #abrir o dicionario
    'login':[], #login da conta. Tipo g-mail ou nome
    'senha':[], #Senha da conta
         'produto':{
              '1': ['computador dell', 5000.0],
              '2': ['Fone Apple', 2000.0],
              '3': ['Mouse Lenovo', 250.0],
              '4': ['Monitor Lenovo', 3000.0]
             } #lista de produtos
} #fehar o dicionario

print('Cadastra-se')

cad_login = input('Cadastre seu login: ') #adiciona ha variavel um valor que será adicionado ao dicionario

cad_senha = input('cadastrase sua senha: ') #adiciona ha variavel um valor que será adicionado ao dicionario
dados['login'].append(cad_login) #primeiro puxa o dado, do dicionario, que quer usar e depois a variavel que vai ser adicionada ao dado

dados['senha'].append(cad_senha
)#primeiro puxa o dado, do dicionario, que quer usar e depois a variavel que vai ser adicionada ao dado

print() #pular linha das ações

#acessar o e-comerce

print('acesse a aplicação')

acesso_login = input('digite seu login para acessar: ') #adiciona a variavel um valor para confirmar o valor que foi adicionado ao dicionario

acesso_senha = input('digite sua senha para acessar: ') #adiciona a variavel um valor para confirmar o valor que foi adicionado ao dicionario

print() #pular linha das ações

if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]: #confirmando os dados que estão dentro das variaveis e do dicionario

    print('Seja bem vindo(a) ao e-commece Z') #verdadeiro/acertou as informações dadas
    #verificar a lista de produto
    print('Produtos: ')

    produto = input(f'''
    {dados['produto']} - escolha - 1 - 2 - 3 - 4 ->>>
    ''') #mostra tudo que está dentro do dicionario produto

    #comprar um produto

    #novas listas
    carrinho = []
    valores = []

    #mostra o produto que foi solicitado
    carrinho.append(dados['produto'][produto][0]) #o primeiro produto é qual está no dicionario/dados e o segundo é a variavel que está na linha 48

    print(carrinho)

    #mostra o valor do produto que foi solicitado
    valores.append(dados['produto'][produto][1])
    #o primeiro produto é qual está no dicionario/dados e o segundo é a variavel que está na linha 48
    
    print(carrinho[0], valores[0])
    
     #paga o produto

     #faz a soma dos produtos
    soma =  sum(valores)

    #mostra o valor a ser pago
    print('Valor a pagar - R$', soma)
    #escolha o pagamento
    pag = input('digite a forma de pagamento')
    print('Forma de pagamento', pag)
    print('Obrigado, volte sempre')



else:

    print('senha incorreta, tente novamente')#falso/errou as informações dadas
