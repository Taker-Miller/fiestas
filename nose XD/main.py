from FiestaCumpleanios import FiestaCumpleanios
from FiestaGala import FiestaGala

def menu():
    opcion = "a"
    while opcion != "d":
        print("¿Qué desea cotizar?")
        print("1 Fiesta Gala")
        print("2 Fiesta Cumpleaños")
        print("d Detener Programa")
        opcion = input("Ingrese una opción: ")
        if opcion in ["1", "2"]:
            cotizar_fiesta(int(opcion))
        elif opcion.lower() == "d":
            print("Chaito")
        else:
            print("La opción ingresada no es válida")

def cotizar_fiesta(opcion: int):
    if opcion == 1:
        cotizar_fiesta_gala()
    else:
        cotizar_fiesta_cumpleanios()

def cotizar_fiesta_gala():
    try:
        personas = int(input("Ingrese número de personas: "))
        if personas > 0:
           cumple = FiestaCumpleanios(personas)
           cumple.calcular_costo_decoracion(decidete("decorar"))
           if decidete("personalizar pastel"):
                texto = input("ingrese texto personalizado")
                cumple.personalizar_pastel(texto)
                cumple.calcular_costo_pastel()
           total = cumple.calcular_costo()
           print(cumple)
           print(f"total: {total}")

            #total = gala.calcular_costo()
            #print(gala)
            #print(f"Total: {total}")
        else:
            print("ERROR.- Debes ingresar un valor mayor a 1")
    except ValueError:
        print("ERROR.- Debes ingresar un valor entero")

def cotizar_fiesta_cumpleanios():
    # TODO: Implementar esta función
    pass

def decidete(texto: str) -> bool:
    decide = "a"
    while decide not in ['s', 'n']:
        decide = input(f"¿Desea {texto}? (s/n): ").lower()
        if decide == "s":
            return True
        elif decide == "n":
            return False
        else:
            print("ERROR.- Solo puedes ingresar s o n")

menu()
