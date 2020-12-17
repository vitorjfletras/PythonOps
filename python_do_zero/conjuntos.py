# Conjuntos são colecções desordenadas de elementos únicos.
# Os elementos não são armazenados em uma ordem específica e confiável.
# Conjuntos não contém elementos repetidos.

print('Loja Stars Wars')

pedidos_dia1 = [ 
    {'Cliente': 'José', 'filme': 'A New Hope'},
    {'Cliente': 'José', 'filme': 'A New Hope'},
    {'Cliente': 'Francisco', 'filme': 'The Empire Strikes Back'},
    {'Cliente': 'Luis', 'filme': ' Revenge of the Sith'},
]


pedidos_dia2 = [
    {'Cliente': 'Marco', 'filme': 'A New Hope'},
    {'Cliente': 'Nuno', 'filme': 'A New Hope'},
    {'Cliente': 'Carlos', 'filme': 'The Empire Strikes Back'},
    {'Cliente': 'Rodrigo', 'filme': ' Revenge of the Sith'},    
]

clientes_dia1 = set()
for pedido in pedidos_dia1:
    clientes_dia1.add(pedido['Cliente'])

print(f'Dia 1: {clientes_dia1}')

clientes_dia2 = set()
for pedido in pedidos_dia2:
    clientes_dia2.add(pedido['Cliente'])

print(f'Dia 2: {clientes_dia2}')

todos_clientes = clientes_dia1 | clientes_dia2
print(f'União: {todos_clientes}')

cliente_comprou_todos_os_dias = clientes_dia1.intersection(clientes_dia2)
print(f'Intersecão: {cliente_comprou_todos_os_dias}')

clientes_diferenca = clientes_dia1 - clientes_dia2
print(f'Diferença: {clientes_diferenca}')