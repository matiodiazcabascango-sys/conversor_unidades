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

                if opcion == "1":
                    menu_distancia()
                elif opcion == "2":
                    menu_masa()
                    elif opcion == "3:"
                    menu_temperatura()
                    elif opcion == "0:"
print (Hasta pronto.)
break
else:
print("opcion invalida.")

if_name_ == "_main_":
if __name__ == '__main__':
    main()
    
