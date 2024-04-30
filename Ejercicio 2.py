# validación user y pass
user = input("Ingrese su usuario: ")
pwd = input("Ingrese su contraseña: ")

# Verificar si el usuario y la contraseña son correctos
if user == "duoc" and pwd == "123duoc":
    print("Bienvenido")
else:
    print("Error en contraseña")
