# Uma lista é uma estrura de dados composta com items organizados de forma linear.

planetas = ['Tatooine', 'Alderaan', 'Yavin IV', 'Hoth']

print(planetas)

print(f'Tamanho da lista de planetas {len(planetas)}')

print(f'Acesso ao primeiro índice da lista: {planetas[0]}')
print(f'Acesso ao segundo índice da lista: {planetas[1]}')
print(f'Acesso ao terceiro índice da lista: {planetas[2]}')
print(f'Acesso ao quarto índice da lista: {planetas[3]}')

print(f'Acesso ao último índice da lista: {planetas[-1]}')
print(f'Acesso ao penúltimo indice da lista: {planetas[-2]}')

# Hoth -> Endor 
planetas[3] = 'Endor'
print(planetas)


print('Adicioanando elementos na lista')
novos_planetas = []
novos_planetas.append('Byss')
novos_planetas.append('Bonadan')
novos_planetas.append('AMBRIA')
novos_planetas.append('Carida')

print(novos_planetas)

print('Acesso a partes da lista')
print(novos_planetas[1:3])
print(novos_planetas[2:])
print(novos_planetas[:3])


print('Ordem alfabetica')
print(novos_planetas)
print(sorted(novos_planetas, key=str.lower))

print('Remover elementos')
print(novos_planetas)
novos_planetas.remove('Carida')
print(novos_planetas)


print('Número de elementos')
print(novos_planetas.count('Bonadan'))
 

print('Inserir elementos')
novos_planetas.insert(0, 'Honoghr')
print(novos_planetas)
novos_planetas.insert(2, 'Kothlis')
print(novos_planetas)


print('Elimina um elemeto da lista e devolve o elemento')
print(novos_planetas)
print('Pop(4)', novos_planetas.pop(4))
print(novos_planetas)

print('Pop()',novos_planetas.pop())
print(novos_planetas)


print('Elimina elementos da lista')
print(novos_planetas)
del novos_planetas[2:]
print(novos_planetas)

numeros = list(range(1,101)) # lista com 100 numeros
print(numeros)
print('-----')
print(len(numeros))
print('-----')
del numeros[1:10]
print(numeros)
del numeros[:10]
del numeros[:10]
print('-----')
print(numeros)