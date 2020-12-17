#    • Concatenação
#        ◦ Somente entre strings
#    • Interpolação
#        ◦ Marcadores (%d, %f, %s)
#            ▪ %d – Inteiro
#            ▪ %f – Float
#            ▪ %s – String
#    • Método format
#        ◦ print(‘Meu nome é {}’:format(nome))
#            ▪ Método f-string (Python 3.6)

planetas = 'Planetas do Star Wars'


planeta1 = 'Tatooine'
planeta2 = 'Alderaan'
planeta3 = 'Yavin IV'
planeta4 = 'Hoth'

lua = True

diametro_planeta1 = 10465.25
diametro_planeta2 = 465
diametro_planeta3 = 12445
diametro_planeta4 = 11582.70


print('')
print('## Concatenação ##')
print('')
mensagem = 'O nome do Planeta é ' + planeta1 
print(mensagem)
mensagem2 = 'O Planeta ' + planeta1 + ' tem o diâmetro de ' + str(diametro_planeta1) + ' kms'
print(mensagem2)


print('')
print('## Interpolação ##')
print('')

print('O tema é %s' %planetas)
print('O planeta %s tem %s kms de diâmetro ' %(planeta1, diametro_planeta1))
print('O planeta %s tem %f kms de diâmetro ' %(planeta1, diametro_planeta1))
print('O planeta %s tem %.2f kms de diâmetro ' %(planeta1, diametro_planeta1)) ## %.2f duas casas decimais
print('O planeta %s tem %d kms de diâmetro ' %(planeta3, diametro_planeta3))
print('O planeta %s tem %d kms de diâmetro ' %(planeta1, diametro_planeta1)) ## Apresenta só o numero inteiro
print('O planeta %s tem %.5d kms de diâmetro ' %(planeta1, diametro_planeta1))


print('')
print('## Método Format ##')
print('')

print('O tema é %s' %planetas)
print('O planeta {} tem {} kms de diâmetro '.format(planeta1, diametro_planeta1))
print('O planeta {} tem {:f} kms de diâmetro '.format(planeta1, diametro_planeta1))
print('O planeta {} tem {:.2f} kms de diâmetro '.format(planeta1, diametro_planeta1))
print('O planeta {} tem {:.3f} kms de diâmetro '.format(planeta3, diametro_planeta3))
print('O planeta {} tem {} kms de diâmetro '.format(planeta1, diametro_planeta1))
print('O planeta {} tem {:03} kms de diâmetro '.format(planeta3, diametro_planeta3))

print('')
print('## Método f-string ##')
print('')

print('O tema é %s' %planetas)
print(f'O planeta {planeta1} tem {diametro_planeta1} kms de diâmetro')
print(f'O planeta {planeta1} tem {diametro_planeta1:f} kms de diâmetro')
print(f'O planeta {planeta1} tem {diametro_planeta1:.2f} kms de diâmetro')
print(f'O planeta {planeta3} tem {diametro_planeta3:.3f} kms de diâmetro')
print(f'O planeta {planeta1} tem {diametro_planeta1} kms de diâmetro')
print(f'O planeta {planeta3} tem {diametro_planeta3:03} kms de diâmetro')
