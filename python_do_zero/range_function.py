numeros=range(20)

print(numeros, type(numeros))
print(list(numeros))

numeros_par = []
numeros_impar = []

for numero in numeros:
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)

print(f'Lista de numeros par {numeros_par}')
print(f'Lista de numeros impar {numeros_impar}')