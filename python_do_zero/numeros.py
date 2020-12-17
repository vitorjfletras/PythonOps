# int (podem ser positvos e negativos)
# float (podem ser positvos e negativos)
# não necessita de ser declarados entre aspas ou duplas, não se usa ponto (.) ou virgula (,) para separar milhar.


print(4)
print(type(4))

print(15.50)
print(type(15.50))

# Função int() - converte um dado para um número inteiro.
diametro_planeta = 11582.70

print('O diâmetro do planeta é : ', diametro_planeta, type(diametro_planeta))
print('O diâmetro do planeta é: ', int(diametro_planeta), type(int(diametro_planeta)))

# Função float() - converte um dado para um número float.
periodo_rotacao=34

print('O periodo de rotação é:  ', periodo_rotacao, type(periodo_rotacao))
print('O periodo de rotação é: ', float(periodo_rotacao), type(float(periodo_rotacao)))

populacao = '10_000'

print('populacao: ', populacao, type(populacao))
print('populacao int: ', int(populacao),type(int(populacao)))
print('populacao float: ', float(populacao),type(float(populacao)))

# Caso a string tiver um ponto (.), tem que se primeiro converter para float e depois para int.
imposto = '29.50'

print('Imposto String', imposto, type(imposto))
print('Imposto float', float(imposto), type(float(imposto)))
print('Imposto int', int(float(imposto)), type(int(float(imposto))))