
nome_estabelicimento= 'Pastelaria DevOps'

pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Empada'

pastel5 = "Carne com queijo"
pastel6 = " Carne com frango "

print('------------')
print('')

print("substituindo caracteres")
print(pastel5.replace('queijo', 'frango'))

print(pastel5.upper())
print(pastel5.lower())

print(pastel5.startswith('Queijo')) # startswith retorna True ou False
print(pastel5.endswith('frango'))

print(pastel5.endswith('queijo'))

print('Pastel 6:', pastel6)

print('Pastel 6:', pastel6.replace('','-')) # Diferente output do print abaixos
print('Pastel 6:', pastel6.replace(' ','-'))

novo_pastel6 = pastel6.strip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

novo_pastel6 = pastel6.strip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)


novo_pastel6 = pastel6.lstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

novo_pastel6 = pastel6.rstrip()
novo_pastel6 = novo_pastel6.replace(' ', '-')
print('Novo Pastel 6: ', novo_pastel6)

print('')

print('## Função LEN ##')
print('Numero de caracteres no Pastel 5: ', len(pastel5))

print('')

print('## Parte da string ##')
print(pastel5[0])
print(pastel5[-1])
# C a r n e
# 0 1 2 3 4
# -5 -4 -3 -2 -1

print('')
print(pastel5[0:3])
print(pastel5[2:5])
print(pastel5[2:])

print('')
print('## Operadores iN / NOT IN ##')
result = 'Frango' in pastel5
print(result)

result = 'Frango' not in pastel5
print(result)
