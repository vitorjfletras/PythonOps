# A função RANGE, frequentemente utilizada com a estrutura de repetição FOR. 

numeros=range(20)

print(numeros, type(numeros))
print(list(numeros))

numeros_par = []
numeros_impar = []

for numero in numeros:
    if numero % 2 == 0: #operador resto da divisão
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(f'Lista de numeros par {numeros_par}')
print(f'Lista de numeros impar {numeros_impar}')