t = (3, 5, 1, 9, 7)
maximo = t[0]
minimo = t[0]
for n in t:
    if n > maximo:
        maximo = n
    if n < minimo:
        minimo = n
print("Máximo:", maximo, "Mínimo:", minimo)
