
nome_estabelicimento= 'Pastelaria DevOps'

pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Empada'

status = True

valor_pastel1 = 6
valor_pastel2 = 5.20
valor_pastel3 = 7
valor_pastel4 = 7.5

print(nome_estabelicimento)

print(pastel1, valor_pastel1, status)
print(pastel2, valor_pastel2, status)
print(pastel3, valor_pastel3, status)
print(pastel4, valor_pastel4, status)

print("")
print('------------------------')

# SOMA
pedido1 = valor_pastel1 + valor_pastel2
print('Valor total Pedido 1: ', pedido1, type(pedido1))

pedido2 = valor_pastel1 + valor_pastel3
print('Valor total Pedido 2: ', pedido2, type(pedido2))

print("")
# Subtracção

custo = 3.0
subtraccao1 = pedido1 - custo
print('Exemplo de Subtracao 1:', subtraccao1)

print("")
# Divisão

preco_medio = (pedido1 + pedido2) / 2
print('Preco medio é: ', preco_medio)

print("")
# Multiplicacao

dias_mes = 22
faturamento = preco_medio * dias_mes
print('Previsão de Faturamento: ', faturamento)

