# Função padrão do Python CSV
import csv

abrir_ficheiro = open('filmes.csv', 'r')

# Leitura
ficheiro_csv = csv.reader(abrir_ficheiro, delimiter=';')

#for line in file_csv:
#    print(line)
#    print(type(line))
#    print(line[0])
#    print(line[2])
#    print(line[2])
#    exit(1)

for [planeta, preco, disponivel] in ficheiro_csv:
    print(f'o filme é {planeta} custa {preco} disponibilidade: {disponivel}')

# EScrita

criar_ficheiro = open('pedidos.csv', 'w', newline='', encoding='utf-8')
escrever_ficheiro = csv.writer(criar_ficheiro, delimiter=';')
cabecalho = ['Planeta', 'preco', 'disponivel']
escrever_ficheiro.writerow(cabecalho)

pedido1 = ['Tatooine', '20', 'disponivel']
escrever_ficheiro.writerow(pedido1)

pedido2 = ['Alderaan', '25', 'disponivel']
escrever_ficheiro.writerow(pedido2)

pedido3 = ['Hoth', '50', 'indisponivel']
escrever_ficheiro.writerow(pedido3)



criar_ficheiro.close()