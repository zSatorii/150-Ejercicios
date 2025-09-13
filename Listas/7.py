numeros = []
i = 0
while i < 7:
    numeros.append(float(input("Ingrese número: ")))
    i += 1

suma = 0
for num in numeros:
    suma += num
print("Lista:", numeros)
print("Suma:", suma)
