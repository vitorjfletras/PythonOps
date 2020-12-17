# A declaração segue o formato aspas simples ('') ou aspas duplas(“”)
# É uma sequência, então podemos saber o tamanho, podemos aceder a um índice, bem como a partes da mesma.
# É imutável, tem seu valor definido na criação.


minha_string = 'olá'
print(minha_string)

minha_string = "olá"
print(minha_string)

minha_string = '''olá'''
print(minha_string)

# Aspas triplas permite extender a string em multiplas linhas
minha_string = """olá, benvindo ao 
           mundo do Python"""
print(minha_string)


str = 'Star Wars'
print('str = ', str)

# Primeiro caracter
print('str[0] = ', str[0])

# último caracter
print('str[-1] = ', str[-1])

# Dividindo entre o 2º ao 5º caracter
print('str[1:5] = ', str[1:5])

