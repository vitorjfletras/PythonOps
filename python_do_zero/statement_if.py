'''

Sistema de calculo de IMC

O IMC é calculado dividindo peso (em kg) pela altura ao quadrado (em metros)

- Menor que 18,5 = Magro 
- Entre 18,5 e 24,9 = Normal
- Entre 25 a 29,9 = Sobrepeso
- Entre 30 a 39,9 = Obesidade
- Maior que 40,00 = Obesidade grave



altura = float(input('Insira o sua altura (Ex: 1.72): '))
peso = float(input('Insira o seu peso (Ex: 75): '))

imc = (peso / (altura**2))
imc = round(imc,2)
#print(imc)

imc = -1
if imc > 0:
    print('OK')
else:
    print('NOK')
'''

## VER QUAL MANEIRA DE FICAR O CODIGO LEGIVEL
imc = 17
if imc < 18.5:
    print(f'O sei IMC é {imc} considerado Magreza')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O sei IMC é considerado Normal')

elif imc >= 25 and imc <= 29.9:
    print(f'O sei IMC é considerado Sobrepeso')

elif imc >= 30 and imc <= 39.9:
    print(f'O sei IMC é considerado Obesidade')

elif imc >= 40.0:
    print(f'O sei IMC é considerado Obesidade Grave')
else:
    print('Padrão não encontrado')













