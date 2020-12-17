# Tuplas similar a uma Lista mas é imutável.

tupla = ()
print(type(tupla))


planeta = ('Tatooine', 10465, True)
print(planeta)
print(planeta[0])
print(planeta[1])
print(planeta[2])
print(planeta[-1]) # último elemento

for plt in planeta:
    print(plt)

print('------')

# atribuição a uma tupla
nome, diametro, lua = planeta
print(nome)
print(diametro)
print(lua)