def verificar_numero(valor):
    if valor > 0:
        return 'P'
    else:
        return 'N'

print(verificar_numero(5))   # P
print(verificar_numero(0))   # N