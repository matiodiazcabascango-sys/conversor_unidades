print ("==Conversor de unidades==")
print("1. Kilometros a Millas")
print("2. Kilogramos a libras")

opcion = input("Seleccione una opcion (1 o 2): ")

if opcion == "1":
    kilometros = float(input("Ingrese kilometros: "))
    millas = kilometros * 0.621371
    print(f"{kilometros} Km equivale a {millas:.2f} millas.")

    def menu_temperatura():
        print("--Temperatura--")
        print("1. celsius a Fahrenheit")
        print("2. Celsius a Kelvin")
        print("0. Volver") 
        opcion = input("Sellecione una opcion:")
else:
    print("Opcion invalida.")