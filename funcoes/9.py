def soma_impares(A, B):
    soma = 0
    for i in range(A, B + 1):
        if i % 2 != 0:
            soma += i
    print("Soma dos ímpares:", soma)

soma_impares(1, 10)