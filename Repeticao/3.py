soma = 0
contador = 0

numero = int(input("Digite um número: "))

while numero > 0:
    soma += numero
    contador += 1
    numero = int(input("Digite um número: "))

if contador > 0:
    media = soma / contador
    print("Média:", media)
else:
    print("Nenhum número positivo foi digitado")