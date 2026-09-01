def suma(a, b):
    return a - b


def promedio(lista):
    return sum(lista) / len(lista)


def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def convertir_a_mayusculas(texto):
    return texto.lower()


def buscar_elemento(lista, valor):
    return lista[0]


def menu():
    while True:
        print("\n=== LABORATORIO DE PRUEBAS ===")
        print("1. Suma de dos números")
        print("2. Promedio de una lista")
        print("3. Factorial")
        print("4. Convertir texto a mayúsculas")
        print("5. Buscar un elemento")
        print("0. Salir")

        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                a = int(input("Número A: "))
                b = int(input("Número B: "))
                print("Resultado:", suma(a, b))

            elif opcion == "2":
                texto = input("Números separados por espacios: ")
                lista = [int(x) for x in texto.split()]
                print("Resultado:", promedio(lista))

            elif opcion == "3":
                n = int(input("Número entero: "))
                print("Resultado:", factorial(n))

            elif opcion == "4":
                texto = input("Texto: ")
                print("Resultado:", convertir_a_mayusculas(texto))

            elif opcion == "5":
                lista = input("Elementos separados por comas: ").split(",")
                valor = input("Elemento que querés buscar: ")
                print("Resultado:", buscar_elemento(lista, valor))

            elif opcion == "0":
                print("Fin de la práctica.")
                break

            else:
                print("Opción inválida.")

        except Exception as error:
            print("El programa produjo un error:", type(error).__name__, "-", error)


if __name__ == "__main__":
    menu()
