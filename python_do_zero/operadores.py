## Operadores aritméticos

#   Operador    operação
#       +       Adição
#       -       Subtração
#       *       Multiplicação
#       /       Divisão
#       **      Power
#       //      Retorna a parte inteira do quociente



numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
power = numero_1 ** numero_2
quociente = numero_1 // numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(power) # 25
print(quociente) # 2


## Operadores de comparação

#       Operador            Descrição
#           ==	              Igual
#           !=	            Não é igual
#           <>	            Não é igual
#            >	             Maior que
#            <	             Menos de
#           >=	            Maior do que ou igual
#           <=	            Menor ou igual

numero_1 = 10
numero_2 = 12

# Output: numero_1 > numero_2 is False
print('numero_1 > numero_2 is',numero_1>numero_2)

# Output: numero_1 < numero_2 is True
print('numero_1 < numero_2 is',numero_1<numero_2)

# Output: numero_1 == numero_2 is False
print('numero_1 == numero_2 is',numero_1==numero_2)

# Output: numero_1 != numero_2 is True
print('numero_1 != numero_2 is',numero_1!=numero_2)

# Output: numero_1 >= numero_2 is False
print('numero_1 >= numero_2 is',numero_1>=numero_2)

# Output: numero_1 <= numero_2 is True
print('numero_1 <= numero_2 is',numero_1<=numero_2)




## Operadores lógicos

#   AND - Se todas as condições forem verdadeiras
#   OR  - Se uma ou outra condição for verdadeira
#   NOT - Ao contrario da condição

 
#   A           B         A AND B
#   V           V           V
#   V           F           F
#   F           V           F
#   F           F           F


#   A       B        A OR B
#   V       V           V
#   V       F           V
#   F       V           V
#   F       F           F


#   A    NOT A
#   V       F
#   V       F
#   F       V
#   F       V


x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)