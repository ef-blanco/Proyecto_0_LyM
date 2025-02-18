import leer
import validar

def mostrar_menu():
    print("\n=============================================")
    print("    Sistema para procesar código de Robot")
    print("=============================================")
    print("1. Escoger el archivo a revisar")
    print("2. Verificar el archivo")
    print("3. Salir")
    print("=============================================")

def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción (1 o 2 o 3): ").strip()

        if opcion == "1":
            print("1) Probar con código completo")
            print("2) Probar con Declaración de Variables")
            print("3) Probar con Procedimientos")
            print("4) Probar con Bloques de código")

            archivo = input("Ingrese el archivo que deseas comprobar: (1,2,3,4): ").strip()

            if archivo == "1":
                contenido = leer.lexer("./ejemplosCodigo/code.txt")
                tokens=leer.resultado(contenido)
                print("\n===================== Contenido del txt en formato de listas sobre listas  =======================")
                for i in tokens:
                    print(i)
                print("====================================================================================================")

            elif archivo == "2":
                contenido = leer.lexer("./ejemplosCodigo/variables.txt")
                tokens=leer.resultado(contenido)
                print("\n===================== Contenido del txt en formato de listas sobre listas  =======================")
                for i in tokens:
                    print(i)
                print("====================================================================================================")

            elif archivo == "3":
                contenido = leer.lexer("./ejemplosCodigo/proc.txt")
                tokens=leer.resultado(contenido)
                print("\n===================== Contenido del txt en formato de listas sobre listas  =======================")
                for i in tokens:
                    print(i)
                print("====================================================================================================")

            elif archivo == "4":
                contenido = leer.lexer("./ejemplosCodigo/bloque.txt")
                tokens=leer.resultado(contenido)
                print("\n===================== Contenido del txt en formato de listas sobre listas  =======================")
                for i in tokens:
                    print(i)
                print("====================================================================================================")

            else:
                print("Opción no válida. Intente nuevamente.")

        elif opcion == "2":
            resultado= validar.validar(tokens)
            print("Al pasar por verificación este código se puede determinar que el contenido ha sido: ", resultado)

        elif opcion == "3":
            print("Saliendo del verificador de código. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()