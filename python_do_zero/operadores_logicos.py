
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

print(nome_estabelicimento)

print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)


print('---------------------------------')
print('')

pagamento_pedido_1_cartao = True
pagamento_pedido_2_cartao = True

print('Precisa de levar dispositivo multibanco?', pagamento_pedido_1_cartao and pagamento_pedido_2_cartao)


pagamento_pedido_1_cartao = True
pagamento_pedido_2_cartao = False

print('Precisa de levar dispositivo multibanco?', pagamento_pedido_1_cartao or pagamento_pedido_2_cartao)

pagamento_pedido_1_cartao = False
pagamento_pedido_2_cartao = False

print('Precisa de levar dispositivo multibanco?', pagamento_pedido_1_cartao and pagamento_pedido_2_cartao)


