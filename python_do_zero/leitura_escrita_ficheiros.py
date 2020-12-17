# Função open(FILE, OPEN)
## FILE: path + nome_do_ficheiro
## mode:
#        r = read - leitura (Por defeito)
#        w = write - escrita, sobescreve o conteúdo se já existir   
#        a = append - escrita, adiciona ao final do ficheiro
#        b = bytes - modo binário


# Leitura
file = open('filmes.txt')
planetas = file.readlines()
for planeta in planetas:
    #print(planeta)
    print(planeta.replace('\n',''))



# Escrita
clientes_star_wars = ['Jośe', 'Carlos', 'Pedro', 'Paulo', 'Mario']
file = open('clientes.txt', 'w')
for cliente in clientes_star_wars:
    print(f'O cliente {cliente} foi adicionado na lista')
    file.write(f'{cliente}\n') # desta forma permite escrever no ficheiro em linha diferentes.

file.close() # Para não deixa o ficheiro aberto para edição.