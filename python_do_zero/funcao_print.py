# A função print() permite 'imprimir' o argumento passado. 

planetas = 'Planetas do Star Wars'


planeta1 = 'Tatooine'
planeta2 = 'Alderaan'
planeta3 = 'Yavin IV'
planeta4 = 'Hoth'

lua = True

diametro_planeta1 = 10465
diametro_planeta2 = 465.20
diametro_planeta3 = 12445
diametro_planeta4 = 11582.70


print(planetas, end='\n==============================\n')
print(planeta1, diametro_planeta1, lua, sep=' ==> ', end='\n\n')
print(planeta2, diametro_planeta2, lua, sep=';', end='\n\n') # Output ponto e virgula (utilizado por csv)

print(planeta2, '\n', diametro_planeta2, '\n', lua)
print(planeta3, diametro_planeta3, lua, sep='\n',end='\n\n')
print(planeta4, diametro_planeta4, lua,sep='\n',end='\n\n')