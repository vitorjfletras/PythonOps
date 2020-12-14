cadapio ={}

print(type(cadapio))

pasltel1 = {'Sabor': 'Frango', 'valor': '4', 'stock': True}

print(pasltel1['Sabor'])
print(pasltel1['valor'])
print(pasltel1['stock'])

# atulizar a cahve Valor para 7
pasltel1['valor'] = 7.00

print(pasltel1)

print(pasltel1.get('quantidade'))

if pasltel1.get('quantidade'):
    print(pasltel1.get('quantidade'))
else:
    pasltel1['quantidade'] = 10

print(pasltel1)

# Retornar em lista

## Retornar as chaves

keys = pasltel1.keys()
print(keys)

for key in keys:
    if key == 'stock':
        print(f'A chave: {key} foi encontrado no dicionario')
    else:
        print('Nao encontrado')


## Retornar os valores

valores = pasltel1.values()
print(valores)

for valor in valores:
    print(f'O elemento {valor} está no dicionario')

## Retornar chave e valor


dict_values = pasltel1.items()
print(dict_values)

for key, value in dict_values:
    print(f'A chave é: {key} e o valor é {value}')
    

## Remover elemnto do dicionario

print(pasltel1)
pasltel1.pop('quantidade')
print(pasltel1)