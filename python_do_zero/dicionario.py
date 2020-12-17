# Dicionários - é um tipo de mapeamento nativo do Python.
# Um mapeamento é uma coleção de associações entre pares de valores
# O primeiro elemento do par é chamado de chave(imutável) e o outro de conteúdo

planetas ={}

print(type(planetas))

planeta = {'Nome': 'Tatooine', 'diametro_planeta': '10465.25', 'Lua': True}

print(planeta['Nome'])
print(planeta['diametro_planeta'])
print(planeta['Lua'])

# Atulizar o valor da chave diametro_planeta para 777.
planeta['diametro_planeta'] = 777
print(planeta)

print(planeta.get('Clima')) # Vai retornar None

# Senão existir a chave Clima, vai criar com o valor 'tropical'
if planeta.get('Clima'):
    print(planeta.get('Clima'))
else:
    planeta['Clima'] = 'tropical'

print(planeta)

# Retornar as chaves
chaves = planeta.keys()
print(chaves)

for chave in chaves:
    if chave == 'Lua':
        print(f'A chave: {chave} foi encontrado no dicionario')
    else:
        print('Nao encontrado')


# Retornar os valores
valores = planeta.values()
print(valores)

for valor in valores:
    print(f'O elemento {valor} está no dicionario')

# Retornar chave e valor
composicao = planeta.items()
print(composicao)

for chave, valor in composicao:
    print(f'A chave é: {chave} e o valor é {valor}')
    
# Remover elemnto do dicionario
print(planeta)
planeta.pop('Clima')
print(planeta)