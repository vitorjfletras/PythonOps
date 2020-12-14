
nome_estabelicimento= 'Pastelaria DevOps'

pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Empada'

status = True

valor_pastel1 = 6.0
valor_pastel2 = 5.20
valor_pastel3 = 7
valor_pastel4 = 7

# print(nome_estabelicimento)
'''
print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)
'''

print('')
print('## Concatenação ##')
print('')
mensagem = 'O nome do estabelecimento é ' + nome_estabelicimento 
print(mensagem)
mensagem2 = 'O pastel de ' + pastel1 + ' custa ' + str(valor_pastel1) + ' euros'
print(mensagem2)


print('')
print('## Interpolação ##')
print('')

print('O nome do estabelecimento é %s' %nome_estabelicimento)
print('O pastel de %s custa %s euros ' %(pastel1, valor_pastel1))
print('O pastel de %s custa %f euros ' %(pastel1, valor_pastel1))
print('O pastel de %s custa %.2f euros ' %(pastel1, valor_pastel1)) ## %.sf duas casas decimais
print('O pastel de %s custa %d euros ' %(pastel3, valor_pastel3))
print('O pastel de %s custa %d euros ' %(pastel1, valor_pastel1)) ## Apresenta só o numero inteiro
print('O pastel de %s custa %.3d euros ' %(pastel1, valor_pastel1)) ## Acrescenta o inteiro para 3 digitos, se fosse 600 output é 600.


print('')
print('## Método Format ##')
print('')

print('O nome do estabelecimento é {}'.format(nome_estabelicimento))
print('O pastel de {} custa {} euros '.format(pastel1, valor_pastel1))
print('O pastel de {} custa {:f} euros '.format(pastel1, valor_pastel1))
print('O pastel de {} custa {:.2f} euros '.format(pastel1, valor_pastel1)) ## %.sf duas casas decimais
print('O pastel de {} custa {:.3f} euros '.format(pastel3, valor_pastel3))
print('O pastel de {} custa {} euros '.format(pastel1, valor_pastel1)) ## Apresenta só o numero inteiro
print('O pastel de {} custa {:03} euros '.format(pastel3, valor_pastel3)) ## Acrescenta o inteiro para 3 digitos, se fosse 600 output é 600.

print('')
print('## Método f-string ##')
print('')

print(f'O nome do estabelecimento é {nome_estabelicimento}')
print(f'O pastel de {pastel1} custa {valor_pastel1} euros')
print(f'O pastel de {pastel1} custa {valor_pastel1:f} euros')
print(f'O pastel de {pastel1} custa {valor_pastel1:.2f} euros')
print(f'O pastel de {pastel3} custa {valor_pastel3:.3f} euros')
print(f'O pastel de {pastel1} custa {valor_pastel1} euros')
print(f'O pastel de {pastel3} custa {valor_pastel3:03} euros')
