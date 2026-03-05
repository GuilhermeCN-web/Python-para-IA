distancia = float(input("Digite a distância a percorrer (km): "))
velocidade = float(input("Digite a velocidade média (km/h): "))

tempo = distancia / velocidade

print(f"Tempo estimado de viagem: {tempo:.2f} horas")