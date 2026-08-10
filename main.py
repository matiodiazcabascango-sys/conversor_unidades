print ("==Conversor de unidades==")
print("1. Kilometros a Millas")
print("2. Kilogramos a libras")

opcion = input("Seleccione una opcion (1 o 2): ")

if opcion == "1":
    kilometros = float(input("Ingrese kilometros: "))
    millas = kilometros * 0.621371
    print(f"{kilometros} Km equivale a {millas:.2f} millas.")
#
# MENU DE TEMPERATURA 
# 
    def menu_temperatura():
        print("--Temperatura--")
        print("1. celsius a Fahrenheit")
        print("2. Celsius a Kelvin")
        print("0. Volver") 
        opcion = input("Sellecione una opcion:")
        if opcion == "1":
            celsius = float(input("Ingrese grados Celcius:"))
            fahrenheut = (celcius *9/5)+32
            print(f"{celcius} C equivale a {fahrenheit:.2f}F.")
        elif opcion == "2":
            celsius = float(input("Ingrese grados Celcius:")) 
            kelvin = celcius + 273.15print(f"{celcius}Cequicale a {kelvin:.2f}K.")
        elif opcion == "0":
            return
        else:
            print("Opcion invalida.") 
        #
        # DESDE AQUI EMPIEZA EL MENU PRINCIPAL  
        #
        def main():
            while True:
                menu_principal()
                opcion = input("Seleccione una opcion:")

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
    