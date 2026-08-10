print ("==Conversor de unidades==")
print("1. Kilometros a Millas")
print("2. Kilogramos a libras")

opcion = input("Seleccione una opcion (1 o 2): ")

if opcion == "1":
    kilometros = float(input("Ingrese kilometros: "))
    millas = kilometros * 0.621371
    print(f"{kilometros} Km equivale a {millas:.2f} millas.")

elif opcion == "2":
    kilogramos = float(input("Ingrese kilogramos: "))
    libras = kilogramos * 2.20462
    print(f"{kilogramos} Kl equivale a {libras:.2f} libras.")
else:
    print("Opcion invalida.")
    
    def menu_temperatura():
    print("== Temperatura ==")
    print("1. Celsius a Fahrenheit")
    print("2. Celsius a Kelvin")
    print("0. Volver")
    opcion = input("Seleccione una opcion: ")