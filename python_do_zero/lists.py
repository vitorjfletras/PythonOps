pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'frango'
pastel4 = 'Vegetais'

cardapio = ['Carne', 'Queijo', 'frango', 'Vegetais']

print(cardapio)

print(f'Tamanho da lista {len(cardapio)}')

print(f'Acessando ao primeiro indice da lista: {cardapio[0]}')
print(f'Acessando ao segundo indice da lista: {cardapio[1]}')
print(f'Acessando ao terceiro indice da lista: {cardapio[2]}')
print(f'Acessando ao quarto indice da lista: {cardapio[3]}')

print(f'Acessando ao ultimo indice da lista: {cardapio[-1]}')
print(f'Acessando ao penultimo indice da lista: {cardapio[-2]}')

# Queijo -> Mussarela
cardapio[1] = 'Mussarela'

print(cardapio)


print('---------')

novo_cardapio = []
print(len(novo_cardapio))
print(type(novo_cardapio))

print('')
print('---------')
print('Adicioanando elementos na lista')
novo_cardapio= []
novo_cardapio.append('Carne')
novo_cardapio.append('Queijo')
novo_cardapio.append('Frango')
novo_cardapio.append('Vegetais')

print(novo_cardapio)



print('')
print('---------')
print('Acessando a partes da lista')
print(novo_cardapio[1:3])
print(novo_cardapio[2:])
print(novo_cardapio[:3])


print('')
print('---------')
print('Ordem alfabetica')
print(novo_cardapio)
print(sorted(novo_cardapio, key=str.lower))



print('')
print('---------')
print('Remover elementos')
print(novo_cardapio)
novo_cardapio.remove('Queijo')
print(novo_cardapio)


print('')
print('---------')
print('Count')
print(novo_cardapio.count('Frango'))

print('')
print('---------')
print('Insert')

novo_cardapio.insert(0, 'Palmito')
print(novo_cardapio)
novo_cardapio.insert(2, 'Mussarela')
print(novo_cardapio)

print('')
print('---------')
print('Pop')

print(novo_cardapio)

print('Pop(4)', novo_cardapio.pop(4))
print(novo_cardapio)

print('Pop()',novo_cardapio.pop())
print(novo_cardapio)

print('')
print('---------')
print('Del')

print(novo_cardapio)
del novo_cardapio[2:]
print(novo_cardapio)



print('')
print('---------')
vendas = []

vendas.append(24.00)
vendas.append(17.00)
vendas.append(48.00)

print(sum(vendas))
print(max(vendas))
print(min(vendas))
print(sum(vendas)/len(vendas))
print(f'{sum(vendas)/len(vendas):.2f}')  ## duas casas decimais


numeros = list(range(1,101)) # lista com 100 numeros
print(numeros)
print('-----')
print(len(numeros))
print('-----')
del numeros[1:10]
print(numeros)
del numeros[:10]
del numeros[:10]
print('-----')
print(numeros)