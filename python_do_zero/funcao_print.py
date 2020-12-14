
nome_estabelicimento= 'Pastelaria DevOps'

pastel1 = 'Carne'
pastel2 = 'Queijo'
pastel3 = 'Frango'
pastel4 = 'Empada'

status = True

valor_pastel1 = 6.0
valor_pastel2 = 5.20
valor_pastel3 = 7
valor_pastel4 = 3.5

# sdef print(*values: object, sep: Optional[Text]=..., end: Optional[Text]=..., file: Optional[_Writer]=..., flush: bool=...)
#print(nome_estabelicimento, end='\n\n')
print(nome_estabelicimento, end='\n==============================\n')
print(pastel1, valor_pastel1, status, sep=' ==> ', end='\n\n')
print(pastel2, valor_pastel2, status, sep=';', end='\n\n') # Simular a saida ponto e virgula (utilizado por csv)

# Sem utilizacao de END e SEP
print(pastel2, '\n', valor_pastel2, '\n', status)
print(pastel3, valor_pastel3, status, sep='\n',end='\n\n')
print(pastel4, valor_pastel4, status,sep='\n',end='\n\n')