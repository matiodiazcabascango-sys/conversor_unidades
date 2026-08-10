# Seccion menu
def menu_principal():
print ("==Conversor de unidades==")
print("1. Distancia")
print("2. Masa")
print("0. Salir")

# Seccion distancia

def menu distancia():
    print("== Distancia ==")
    print("1. Kilometros a milas")
    print("2. Metros a pies")
    print("0. Volver")
    opcion = input("Seleccione una opcion:")

if opcion == "1":
    kilometros = float(input("Ingrese kilometros: "))
    millas = kilometros * 0.621371
    print(f"{kilometros} Km equivale a {millas:.2f} millas.")
elif opcion == "2":
    metros = float(input("Ingrese Metros: "))
    pies = metros * 3.28084
    print(f"{metros} m equivale a {pies:.2f} ft.")
elif opcion == "0":
    return
else:
    print("Opcion invalida")

elif opcion == "2":
    kilogramos = float(input("Ingrese kilogramos: "))
    libras = kilogramos * 2.20462
    print(f"{kilogramos} Kl equivale a {libras:.2f} libras.")
else:
    print("Opcion invalida.")