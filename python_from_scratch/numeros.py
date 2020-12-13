print(4)
print(type(4))


print('-------------------------')

print(15.50)
print(type(15.50))

print("", end='\n\n')

print('====================================================')
print('Numeros apartir das funções INT e FLOAT')
print('====================================================', end='\n\n')

preco_ingrediente = 14.70

print('Preço do ingrediente float: ', preco_ingrediente, type(preco_ingrediente))
print('Preço do ingrediente float: ', int(preco_ingrediente), type(int(preco_ingrediente))) # Concatenação

print("", end='\n\n')

total_stock=34

print('Total stock int: ', total_stock, type(total_stock))
print('Total stock float: ', float(total_stock), type(float(total_stock)))

print("", end='\n\n')

faturamento = '10_000'

print('Faturamento: ', faturamento, type(faturamento))
print('Faturamento int: ', int(faturamento),type(int(faturamento)))
print('Faturamento float: ', float(faturamento),type(float(faturamento)))


print("", end='\n\n')

imposto = '29.50'

print('Imposto String', imposto, type(imposto))
print('Imposto float', float(imposto), type(float(imposto)))
print('Imposto int', int(float(imposto)), type(int(float(imposto))))  #### Tentar converter valor de String para INT nao vai funcionar, devido a ter um ponto (.). 
                                                                      #### tem de ser de string para float e depois int.