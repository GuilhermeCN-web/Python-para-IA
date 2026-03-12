contador = 0
numero = int(input("Digite um número: "))

while numero != 0:
    if 100 <= numero <= 200:
        contador += 1
    
    numero = int(input("Digite um número: "))

print("Quantidade de números entre 100 e 200:", contador)