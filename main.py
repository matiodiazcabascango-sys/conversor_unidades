# Seccion menu
def menu_principal():
    print("==Conversor de unidades==")
    print("1. Distancia")
    print("2. Masa")
    print("3. Temperatura")
    print("0. Salir")

# Seccion distancia

def menu_distancia():
    print("== Distancia ==")
    print("1. Kilometros a millas")
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

# Seccion masa

def menu_masa():
    print("--- Masa ---")
    print("1. Kilogramos a libras")
    print("2. Kilogramos a onzas")
    print("0. Volver")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        kg = float(input("Ingrese kilogramos: "))
        libras = kg * 2.20462
        print(f"{kg} Kg equivale a {libras:.2f} libras.")
    elif opcion == "2":
        kg = float(input("Ingrese kilogramos: "))
        onzas = kg * 35.274
        print(f"{kg} Kg equivale a {onzas:.2f} onzas.")
    elif opcion == "0":
        return
    else:
        print("Opcion invalida.")

#Seccion temperatura

def menu_temperatura():
    print("--- Temperatura ---")
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

def main():
    while True:
        menu_principal()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_distancia()
        elif opcion == "2":
            menu_masa()
        elif opcion == "3":
            menu_temperatura()
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
