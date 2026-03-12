contador = 0
sexo = input("Digite o sexo (M/F) ou 0 para sair: ")

while sexo != "0":
    if sexo == "m" or sexo == "M":
        contador += 1
    
    sexo = input("Digite o sexo (M/F) ou 0 para sair: ")

print("Quantidade de pessoas do sexo masculino:", contador)