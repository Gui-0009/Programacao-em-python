# e-commerce 
# lista de produtos
# lista de valores 
# poder comprar um produto


print('E-COMMERCE')
#listas dos produtos, valores, carrinho e o valor a ser pago.
#O primeiro 'valor' está vazio para a lista começar pelo 1.
lista_prod = ['','hd', 'pen-drive','fone', 'carregador']
#O primeiro 'valor' está com o umero '0' para a lista começar pelo 1.
lista_valores = [0,450.0, 100.0,350.0,90.0]
#'carrinho' e 'meu-valor' estão vazios pq a compra não deu inicio
carrinho = []
meu_valor = []
#separar o enunciado dos produtos/valor
print('***' * 20)
#está mostrando a 'praileira' dos produtos
#id:junto com o 'index' mostra a posição do 'produto' que está na varievl 'lista_prod'. produto: mostra o nome do produto que está na variavel 'lista_prod'. valor R$: mostra o valor do produto que está na variavel 'lista_valor'.
print(f'''
PRODUTOS:
ID            PRODUTOS       VALOR R$
{lista_prod.index('hd')}                 {lista_prod[1]}        {lista_valores[1]}
{lista_prod.index('pen-drive')}          {lista_prod[2]}        {lista_valores[2]}         
{lista_prod.index('fone')}               {lista_prod[3]}        {lista_valores[3]}
{lista_prod.index('carregador')}         {lista_prod[4]}        {lista_valores[4]}
''')

#separar a 'pratileira' dos produtos/valor
print('***' * 20)


#essas 3 partes irão acrecentar a minha variavel 'carinho' o nome do produto e na minha variavel 'meu_valor' as somas dos valores dos produtos. Ex: (carinho - 1, 2, 3. valor - 50.0 + 40.00 + 20.00)
produto1 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto1])
meu_valor.append(lista_valores[produto1])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )


produto2 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto2])
meu_valor.append(lista_valores[produto2])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )


produto3 = int(input('Digite o ID do produto: '))
carrinho.append(lista_prod[produto3])
meu_valor.append(lista_valores[produto3])
print('SEUS PRODUTOS - ', carrinho)
total = sum(meu_valor)
print('Total R$', total )

#Essa pare dá formas de pagamento.
formas_pagamentos =  ['pix','cc','cd']
print('escolha a  forma de pagamento: ', formas_pagamentos)
escolhe_forma = input('Digite a forma de pagamento: ')
indice = formas_pagamentos.index(escolhe_forma)
print('Forma de pagamento: ', formas_pagamentos[indice])
print('Obrigada volte sempre! ')


