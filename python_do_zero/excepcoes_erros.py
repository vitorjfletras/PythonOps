# Excepções

try:
    with open('ficheiro.txt', 'r') as file:
        print(file)
except Exception as err:
    print('Ficheiro não encontrado')


print('A execução do programa continua')


fim = False
while not fim:
    try:
        a = input ("Digite um numero: ")
        b = input ("Digite outro numero: ")
        print(a/b)
        fim = True
    except ZeroDivisionError:
        print("Você tentou dividir por zero. Tente novamente")
    except TypeError:
        print('Você usou um valor não numérico. Tente novamente')