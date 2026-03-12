contador = 0
numero = int(input("Digite um número: "))

while numero > 0:
    contador += 1
    numero = int(input("Digite um número: "))

print("Quantidade de números digitados:", contador)