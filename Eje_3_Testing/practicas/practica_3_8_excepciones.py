"""Práctica 3-8: manejar excepciones en un selector de misiones."""

misiones = [
    "Rescatar al robot",
    "Explorar el laboratorio",
    "Recuperar la contraseña",
]

while True:
    print("\n=== MISIONES DISPONIBLES ===")
    print("1.", misiones[0])
    print("2.", misiones[1])
    print("3.", misiones[2])

    entrada = input("Elegí una misión o S para salir: ")

    if entrada in ("s", "S"):
        break

    try:
        opcion = int(entrada)
        mision_seleccionada = misiones[opcion - 1]

        print("\n########################################")
        print("### MISIÓN SELECCIONADA")
        print("###", mision_seleccionada)
        print("########################################\n")
        break

    except ValueError:
        print("La opción debe ser un número.")

    except IndexError:
        print("No existe esa misión.")

print("Selector cerrado.")

