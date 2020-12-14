print('Seja bem vindo a Pastelaria DevOps')
print('O que deseja?')


'''
0 - estabelecimento fechado
1 - estabelecimento aberto
'''

'''
status = 1

while status ==  1:
    item = input('Qual é o sabor do pastel que deseja?: ')
    print(f'Pedido confirmado')

    status = int(input('Digite 1 para novos pedidos 0 para encerrar: ')) ## Tem que ser convertido para INTEIRO.
'''

contador = 0
quantidade_de_pedidos = 3

while contador < quantidade_de_pedidos:
    item = input('Qual é o sabor do pastel que deseja?: ')
    print(f'Pedido confirmado')
    contador += 1 ## contador = contador +1
