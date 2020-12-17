# A Função input() permite receber dados ou valores do utilizador através do teclado. 

print('Seja bem vindo ao Mundo Star Wars')

item = input('Qual é o filme que pretende ver: ')
print(f'O filme escolhido foi: {item} - {type(item)}')

pedido = (input(f'O filme {item} tem um  custo de 10 euros. Pretende continuar? '))
print(f'Pedido confirmado: {pedido} - {type(pedido)}')
