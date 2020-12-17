# Funçoes
# Variaveis locais e globais

def mensagem_motd(nome):
    print(f'Bem vindo a Loja {nome}')

mensagem_motd(nome='Star Wars')


def pedidos(cliente, filme):
    pedido_cliente = f'o cliente {cliente} pediu o filme {filme}'
    return pedido_cliente


pedido_1 = pedidos(cliente='Luis', filme='The Clone Wars') 
pedido_2 = pedidos('Carlos', 'Revenge of the Sith')
print(pedido_1)
print(pedido_2)