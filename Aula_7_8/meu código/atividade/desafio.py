produto_valor= {
    'livro': {
        'a':50.0,
        'b':80.0
    },
    'tablet':{
        'x':200.0,
        'y':150.0
},
    'fone':{
        'tx':25.0,
        'ty':50.0
    }
}
meus_produtos ={
    'carrinho':[],
    'valor':[]
}
#está especificando que a seção do produto é 'tal'. Ex: seção: tablet; produto: x
secao1 = input('digite a seção')
#está dizendo qual produto está sendo solicitado
produto1 = input('produto1')
#está especificando que a seção do produto é 'tal'. Ex: seção: tablet; produto: x
secao2 = input('digite a seção')
produto2 = input('produto2')
print(produto_valor)
#Ira adicionar a variavel 'carrinho' o produto que foi solicitado da variavel 'produto1'
meus_produtos['carrinho'].append(produto1)
#Ira adicionar a variavel 'carrinho' o produto que foi solicitado da variavel 'produto2'
meus_produtos['carrinho'].append(produto1)
#Ira adicionar a variavel 'carrinho' o valor do produto que está na variavel 'produto_valor' e entre
meus_produtos['valor'].append(produto_valor[secao1][produto1])
meus_produtos['valor'].append(produto_valor[secao2][produto2])
print(meus_produtos)
total = sum(meus_produtos['valores'])
print('total - R$', total)
lista_pag =  ['pix', 'cc', 'cd']
forma = input('digite a forma de pagamento: ')
print('forma de pagamento> ', forma)
print('Obrigada volte sempre! ')