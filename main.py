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

    if opcion == "1":
        celsius = float(input("Ingrese grados Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} C equivale a {fahrenheit:.2f} F.")

        elif opcion == "2":
        celsius = float(input("Ingrese grados Celsius: "))
        kelvin = celsius + 273.15
        print(f"{celsius} C equivale a {kelvin:.2f} K.")
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")