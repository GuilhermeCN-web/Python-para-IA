def eh_multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

print(eh_multiplo(10, 2))  # True
print(eh_multiplo(10, 3))  # False