# Validador de contraseñas
contraseña = "MiClave123" # Contraseña a validar
longitud_minima = 8 # Mínimo de caracteres
print("Contraseña a validar:", contraseña)
print("Longitud de la contraseña:", len(contraseña))
if len(contraseña) >= longitud_minima:
    print("7 La contraseña tiene la longitud correcta")
if contraseña.islower(): # Si todo está en minúsculas
    print("1")