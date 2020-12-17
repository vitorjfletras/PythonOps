# A função enumarate() retorna um objeto iterável
# retorna uma tupla de dois elementos a cada iteração: um número sequencial e um item da sequência correspondente.

filmes = ['The Rise of Skywalker', 'The Phantom Menace', 'Attack of the Clones', 'A STAR WARS STORY', 'THE LAST JEDI', 'THE FORCE AWAKENS']

print('Bem vindo a Loja Star Wars')
print('Veja a nossa lista de filmes')
print('----------')

for indice, tipo in enumerate(filmes):
    print(f'{[indice]}: {tipo}')

print(f'O tipo de dados indice é: {type(indice)}, O tipo de dados filmes é: {type(filmes)}')


#
### Tentar fazer um cilo que ao introduzir 0 sai!!

opcao = int(input('Introduza o número correspondente ao filme que pretende: '))

if opcao >= 0 and opcao <= len(filmes):
    print(f'O filme escolhido foi: {filmes[opcao]}')
else:
    print('Opção invalida')