print('Seja bem vindo a Loja Star Wars')
print('O que deseja?')

'''
0 - Loja Star Wars
1 - Loja Star Wars
'''

contador = 0
quantidade_de_pedidos = 3

while contador < quantidade_de_pedidos:
    item = input('Qual é o filme que deseja?: ')
    print(f'Pedido confirmado, filme {item}')
    contador += 1 ## contador = contador +1
