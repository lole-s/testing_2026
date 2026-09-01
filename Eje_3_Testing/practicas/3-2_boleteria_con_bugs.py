def calcular_precio(edad):
    if edad <= 12:
        return 3000
    if edad < 18:
        return 4500
    return 6000


def aplicar_descuento(precio, codigo):
    if codigo == "PROA10":
        return precio * 0.80
    return precio


def puede_ingresar_solo(edad, esta_acompanado):
    if edad < 12 and not esta_acompanado:
        return False
    return True


def leer_respuesta_si_no(mensaje):
    respuesta = input(mensaje).strip().lower()
    return respuesta in ("s", "si", "sí")


def menu():
    while True:
        print("\n=== BOLETERÍA PROA ===")
        print("1. Consultar precio")
        print("2. Aplicar código de descuento")
        print("3. Consultar si puede ingresar solo/a")
        print("0. Salir")

        opcion = input("Elegí una opción: ").strip()

        try:
            if opcion == "1":
                edad = int(input("Edad: "))
                print("Precio: $", calcular_precio(edad), sep="")

            elif opcion == "2":
                precio = float(input("Precio original: $"))
                codigo = input("Código: ").strip()
                print("Precio final: $", aplicar_descuento(precio, codigo), sep="")

            elif opcion == "3":
                edad = int(input("Edad: "))
                acompanado = leer_respuesta_si_no("¿Está acompañado/a? (s/n): ")
                if puede_ingresar_solo(edad, acompanado):
                    print("Ingreso permitido.")
                else:
                    print("No puede ingresar sin acompañante.")

            elif opcion == "0":
                print("Fin de la práctica.")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Dato inválido: se esperaba un número.")


if __name__ == "__main__":
    menu()
