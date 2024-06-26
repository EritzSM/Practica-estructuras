from Libros import Libro 
from Biblioteca import GestorLibros
def mostrar_menu():
    print("Bienvenido a la biblioteca")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Buscar libros por género")
    print("4. Buscar libro disponibles por título")
    print("5. Buscar libro disponibles por autor")
    print("6. Buscar libro disponibles por año de publicación")
    print("7. Listar libros disponibles para alquilar")
    print("8. Listar libros que se encuentran alquilados")
    print("9. Listar libros disponible por género")
    print("10. Listar libros alquilados por género")
    print("11. Alquilar por género libro")
    print("12. Alquilar libro")
    print("13. Devolver libro")
    print("14. Calcular descuento")
    print("15. Calcular ingresos totales")
    print("16. Intercambiar libros deteriorados")
    print("0. Salir")
    
def main():
    gestor = GestorLibros()
    
    libro1 = Libro(1, "Romance", "Jose Luis Díaz", "Los rios profundos el amor", 2015, 2000)
    libro2 = Libro(2, "Ficción", "Tomás Carrasquilla", "De sobremesa", 1949, 3200)
    libro3 = Libro(3, "Ficción", "Gabriel García Márquez", "Cien años de soledad", 1967, 2500)
    libro4 = Libro(4, "História", "Álvaro Cepeda", "La casa grande", 1966, 1800)
    libro5 = Libro(5, "História", "Arturo Alape", "El bogotazo", 1986, 1000)
    gestor.agregar_libro(libro1)
    gestor.agregar_libro(libro2)
    gestor.agregar_libro(libro3)
    gestor.agregar_libro(libro4)
    gestor.agregar_libro(libro5)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar libro
            numero_libro = int(input("Ingrese el número del libro: "))
            genero = input("Ingrese el género del libro: ")
            autor = input("Ingrese el autor del libro: ")
            titulo = input("Ingrese el título del libro: ")
            ano_publicacion = int(input("Ingrese el año de publicación del libro: "))
            tarifa_diaria = float(input("Ingrese la tarifa diaria de alquiler del libro: "))
            libro_nuevo = Libro(numero_libro, genero, autor, titulo, ano_publicacion, tarifa_diaria)
            gestor.agregar_libro(libro_nuevo)
            

        elif opcion == "2":
            # Eliminar libro
            numero_libro = int(input("Ingrese el número del libro a eliminar: "))
            if gestor.eliminar_libro(numero_libro):
                print("Libro eliminado correctamente")
            else:
                print("El libro no fue encontrado en la biblioteca")

        elif opcion == "3":
            # Buscar libros por género
            genero = input("Ingrese el género del libro a buscar: ")
            cantidad, libros_encontrados = gestor.buscar_por_genero(genero)
            if cantidad > 0:
                print(f"Se encontraron {cantidad} libros del género '{genero}':")
                current_node = libros_encontrados.head
                while current_node:
                    print(current_node.value)
                    current_node = current_node.next
            else:
                print(f"No se encontraron libros del género '{genero}'.")

        if opcion == "4":
            # Buscar por título
            titulo = input("Ingrese el título del libro a buscar: ")
            libro, disponibilidad = gestor.buscar_por_titulo(titulo)
            if libro:
                print(f"Libro encontrado: {libro}")
            else:
                print("Libro no encontrado.")

        elif opcion == "5":
            # Buscar por autor
            autor = input("Ingrese el autor de los libros a buscar: ")
            libros_encontrados = gestor.buscar_por_autor(autor)
            if libros_encontrados:
                print("Libros encontrados:")
                current_node = libros_encontrados.head
                while current_node:
                    libro = current_node.value
                    print(f"{libro} ")
                    current_node = current_node.next
            else:
                print("No se encontraron libros del autor especificado.")

        elif opcion == "6":
            # Buscar por año de publicación
            ano_publicacion = int(input("Ingrese el año de publicación del libro a buscar: "))
            libros_encontrados = gestor.buscar_por_ano_publicacion(ano_publicacion)
            if libros_encontrados:
                print("Libros encontrados:")
                current_node = libros_encontrados.head
                while current_node:
                    libro = current_node.value
                    print(f"{libro} ")
                    current_node = current_node.next
            else:
                print("No se encontraron libros publicados en el año especificado.")



        elif opcion == "7":
            # Listar libros disponibles
            libros_disponibles = gestor.listar_disponibles()
            print("Libros disponibles:")
            for libro in libros_disponibles:
                print(libro)

        elif opcion == "8":
            # Listar libros alquilados
            libros_alquilados = gestor.listar_alquilados()
            print("Libros alquilados:")
            for libro in libros_alquilados:
                print(libro)

        elif opcion == "9":
            # Listar libros disponibles por género
            genero = input("Ingrese el género de los libros disponibles a listar: ")
            libros_disponibles = gestor.listar_disponibles_por_genero(genero)
            print(f"Libros disponibles del género '{genero}':")
            for libro in libros_disponibles:
                print(libro)

        elif opcion == "10":
            # Listar libros alquilados por género
            genero = input("Ingrese el género de los libros alquilados a listar: ")
            libros_alquilados = gestor.listar_alquilados_por_genero(genero)
            print(f"Libros alquilados del género '{genero}':")
            for libro in libros_alquilados:
                print(libro)
        
        elif opcion == "11":
            #Alquilar libro por género
            genero = input("Ingrese el género del libro a listar: ")
            gestor.alquilar_libro_por_genero(genero)


        elif opcion == "12":
            # Alquilar libro
            numero_libro = int(input("Ingrese el número del libro a alquilar: "))
            if gestor.alquilar_libro(numero_libro):
                print("Libro alquilado correctamente")
            else:
                print("El libro no está disponible para alquilar")

        elif opcion == "13":
            # Devolver libro
            numero_libro = int(input("Ingrese el número del libro a devolver: "))
            if gestor.devolver_libro(numero_libro):
                print("Libro devuelto correctamente")
            else:
                print("El libro no está registrado como alquilado")

        elif opcion == "14":
            # Calcular descuento
            cantidad_libros_alquilados = int(input("Ingrese la cantidad de libros alquilados por el usuario: "))
            descuento = gestor.calcular_descuento(cantidad_libros_alquilados)
            print(f"Tiene un descuento de {descuento} pesos")

        elif opcion == "15":
            # Calcular ingresos totales
            ingresos_totales = gestor.calcular_ingreso_total()
            print(f"Ingresos totales hasta el momento: {ingresos_totales}")

        elif opcion == "16":
            id_libro = int(input("Ingrese el ID del libro que desea intercambiar: "))

            # Buscar el libro en la biblioteca
            libro_a_intercambiar = None
            current = gestor.biblioteca.head
            while current:
                if current.value.numero_libro == id_libro:
                    libro_a_intercambiar = current.value
                    break
                current = current.next

            if libro_a_intercambiar:
                
                print("Ingrese la información del nuevo libro:")
                id_libro_nuevo = input("Nuevo Id: ")
                genero = input("Género: ")
                autor = input("Autor: ")
                titulo = input("Título: ")
                ano_publicacion = int(input("Año de Publicación: "))
                tarifa_diaria = float(input("Tarifa Diaria de Alquiler: "))

                nuevo_libro = Libro(id_libro_nuevo, genero, autor, titulo, ano_publicacion, tarifa_diaria)


                if gestor.intercambiar_libro_deteriorado(id_libro, nuevo_libro):
                    print("Intercambio realizado con éxito.")
                else:
                    print("No se pudo realizar el intercambio. No se encontró un libro con el ID especificado.")
            else:
                print("No se encontró ningún libro con el ID especificado.")

            print("\nLibros disponibles después del intercambio:")
            for libro in gestor.biblioteca:
                print(libro.value)


        elif opcion == "0":
            print("Gracias por usar la biblioteca. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()