# JSON
# Serializar - processo de transformar objectos em JSON.
    # dump() - transforma o objecto em python para escrever em um JSON.
    # dumps()- transforma o objecto python para uma string em formato JSON.
    #          pode ser utilizado para enviar dados JSON para uma API.
# Deserializar - processo de transformar JSON para objectos.
    # load() - transforma um objecto JSON para um obejecto em python.
    # loads() - transforma um objecto JSON para um objecto python, para permitir a sua manipulação.
    

import json


pedidos_clientes = {
    "sitio": "Loja Star Wars",
    "pedidos": [
        {
            "cliente": "Luis",
            "valor": "50.00"

        },
        {
            "cliente": "Carlos",
            "valor": "24.00"
        }
        
    ]
}

print(type(pedidos_clientes))
print(pedidos_clientes)


json_data_ser = json.dumps(pedidos_clientes, indent=4) # com a opção indent=4 (identação JSON)
print(type(json_data_ser))
print(json_data_ser)

# Nova forma de abrir ficheiros
with open('pedidos_clientes.txt', 'w') as file:
    json.dump(pedidos_clientes, file, indent=4)

print('Fim da Serialização')



## DESERIALIZAÇÂO

with open('clientes_pedidos.json') as file:
    json_data_des = json.load(file)

print(type(json_data_des))
print(json_data_des)


json_data_dumps = json.dumps(json_data_des)
print(type(json_data_des))
print(json_data_des)


json_string = '{"sitio": "Loja Star Wars", "pedidos": [{"cliente": "Luis", "valor": "50.00"}, {"cliente": "Carlos", "valor": "24.00"}]}'

print(type(json_string))

json_data_string = json.loads(json_string)
print(type(json_data_string))
print(json_data_string)


