cardapio = ['Carne', 'Queijo', 'frango', 'Vegetais', 'Pizza', 'Tremocos', 'sapateira']

print('Pastelaria DevOps')
print('Veja o nosso cardapio')
print('----------')

for indice, recheio in enumerate(cardapio):
    print(f'{[indice]}: {recheio}')



print(f'O tipo de dados indice é: {type(indice)}, O tipo de dados do cardapio é: {type(cardapio)}')


## Tentar fazer um cilo que ao introduzir 0 sai!!

opcao = int(input('Introduza o número correspondente ao sabor desejado: '))

if opcao >= 0 and opcao <= len(cardapio):
    print(f'O sabor escolhido foi {cardapio[opcao]}')
else:
    print('Opção invalida')