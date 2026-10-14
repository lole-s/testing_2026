"""Laboratorio de la clase 3-6. Contiene errores lógicos intencionales."""


def precio_entrada(edad):
    if edad >= 13:
        return 2000
    elif edad >= 18:
        return 3500
    return 0


def precio_recital(es_estudiante, compra_anticipada):
    precio = 12000
    if es_estudiante:
        precio = precio * 0.75
    if compra_anticipada:
        precio = precio * 0.90
    return precio


def puntaje_speedrun(monedas, segundos):
    puntos = monedas * 100
    if segundos < 60:
        puntos += 500
    elif monedas >= 10:
        puntos += 300
    return puntos


def total_delivery(subtotal, cupon):
    total = subtotal
    if cupon == "PROA20" and subtotal >= 10000:
        total = total * 0.80

    if subtotal >= 15000:
        envio = 0
    else:
        envio = 2000

    return total + envio


def menu():
    while True:
        print("\n=== FUNCIONES BAJO SOSPECHA ===")
        print("1. Precio de una entrada")
        print("2. Precio de una entrada de recital")
        print("3. Calcular un pedido de delivery")
        print("4. Calcular el puntaje de un speedrun")
        print("0. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            edad = int(input("Edad: "))
            print("Precio devuelto:", precio_entrada(edad))
        elif opcion == "2":
            estudiante = input("¿Es estudiante? (s/n): ").strip().lower() == "s"
            anticipada = input("¿Compra anticipada? (s/n): ").strip().lower() == "s"
            print("Precio devuelto:", precio_recital(estudiante, anticipada))
        elif opcion == "3":
            subtotal = float(input("Subtotal: "))
            cupon = input("Cupón (Enter si no tiene): ").strip().upper()
            print("Total devuelto:", total_delivery(subtotal, cupon))
        elif opcion == "4":
            monedas = int(input("Monedas: "))
            segundos = int(input("Tiempo en segundos: "))
            print("Puntaje devuelto:", puntaje_speedrun(monedas, segundos))
        elif opcion == "0":
            print("Fin del laboratorio.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
