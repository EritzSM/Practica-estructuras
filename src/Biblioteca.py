from Libros import LinkedList, Node
class GestorLibros:
    def __init__(self):
        self.biblioteca = LinkedList()
        self.ingreso_total = 0

    def agregar_libro(self, libro):
        current = self.biblioteca.head
                                                                                                                            # V
        while current:
            if current.value.numero_libro == libro.numero_libro:
                print("Este libro ya existe en la biblioteca.")
                return
            current = current.next

                                                                                                                            # B
        current = self.biblioteca.head
        Ultimo_libro_por_genero = None
        while current:
            if current.value.genero == libro.genero:
                Ultimo_libro_por_genero = current
            current = current.next

                                                                                                                            # I
        if Ultimo_libro_por_genero:
            new_node = Node(libro)
            new_node.next = Ultimo_libro_por_genero.next
            Ultimo_libro_por_genero.next = new_node
            if Ultimo_libro_por_genero == self.biblioteca.tail:
                self.biblioteca.tail = new_node
        else:
            self.biblioteca.append(libro)

        print("Libro agregado correctamente.")

    def eliminar_libro(self, numero_libro):
        current = self.biblioteca.head
        prev = None
        while current:
            if current.value.numero_libro == numero_libro:
                if prev:
                    prev.next = current.next
                else:
                    self.biblioteca.head = current.next
                self.biblioteca.length -= 1
                return True
            prev = current
            current = current.next
        return False

    def buscar_por_genero(self, genero): 
        libros_encontrados = LinkedList()  
        cantidad = 0
        current = self.biblioteca.head
        while current:
            if current.value.genero == genero:
                cantidad += 1
                libros_encontrados.append(current.value)  
            current = current.next
        return cantidad, libros_encontrados

    def buscar_por_titulo(self, titulo):
        current = self.biblioteca.head
        while current:
            if current.value.titulo == titulo:
                return current.value, "Disponible" if current.value.disponible else "No disponible"
            current = current.next
        return None, "No se encontró el libro"

    def buscar_por_autor(self, autor):
        libros_encontrados = LinkedList()  
        current = self.biblioteca.head
        while current:
            if current.value.autor == autor: 
                libros_encontrados.append(current.value)  
            current = current.next
        return libros_encontrados

    def buscar_por_ano_publicacion(self, ano_publicacion):
        libros_encontrados = LinkedList()  
        current = self.biblioteca.head
        while current:
            if current.value.ano_publicacion == ano_publicacion:
                libros_encontrados.append(current.value)  
            return libros_encontrados

    def listar_disponibles(self):
        current = self.biblioteca.head
        libros_disponibles = LinkedList()
        while current:
            if current.value.disponible:
                libros_disponibles.append(current.value)
            current = current.next
        return libros_disponibles

    def listar_alquilados(self):
        current = self.biblioteca.head
        libros_alquilados = LinkedList()
        while current:
            if not current.value.disponible:
                libros_alquilados.append(current.value)
            current = current.next
        return libros_alquilados

    def listar_disponibles_por_genero(self, genero):
        libros_disponibles = LinkedList()  
        current = self.biblioteca.head
        while current:
            if current.value.genero == genero and current.value.disponible:
                libros_disponibles.append(current.value)  
            current = current.next
        return libros_disponibles

    def listar_alquilados_por_genero(self, genero):
        libros_alquilados = LinkedList() 
        current = self.biblioteca.head
        while current:
            if current.value.genero == genero and not current.value.disponible:
                libros_alquilados.append(current.value)
            current = current.next
        return libros_alquilados

    def alquilar_libro_por_genero(self, genero):
        libros_disponibles_genero = self.listar_disponibles_por_genero(genero)
        if libros_disponibles_genero:
            print(f"Libros disponibles del género '{genero}':")
            for libro in libros_disponibles_genero:
                print(libro)

                id_libro = int(input("Ingrese el ID del libro que desea alquilar: "))
                alquiler_exitoso = self.alquilar_libro(id_libro)
                if alquiler_exitoso:
                    print("Libro alquilado con éxito.")
                    return True
                else:
                    print("No se pudo alquilar el libro.")
                    return False
            else:
                print("Operación cancelada.")
                return False
        else:
            print(f"No hay libros disponibles del género '{genero}'.")
            return False
    
    def alquilar_libro(self, numero_libro):
        current = self.biblioteca.head
        while current:
            if current.value.numero_libro == numero_libro and current.value.disponible:
                current.value.disponible = False
                self.ingreso_total += current.value.tarifa_diaria
                return True
            current = current.next
        return False

    def devolver_libro(self, numero_libro):
        current = self.biblioteca.head
        while current:
            if current.value.numero_libro == numero_libro and not current.value.disponible:
                current.value.disponible = True
                return True
            current = current.next
        return False

    def calcular_descuento(self, cantidad_libros):
        if cantidad_libros >= 2:
            descuento = self.ingreso_total * 0.1
            return descuento
        else:
            return 0

    def calcular_ingreso_total(self):
        return self.ingreso_total

    def intercambiar_libro_deteriorado(self, numero_libro, nuevo_libro):
        current = self.biblioteca.head
        while current:
            if current.value.numero_libro == numero_libro and current.value.disponible:
                nuevo_nodo = Node(nuevo_libro)  # Crear un nuevo nodo con el nuevo libro
                nuevo_nodo.next = current.next  # Enlazar el nuevo nodo con el siguiente nodo
                if current == self.biblioteca.head:  # Si el nodo a reemplazar es el primero
                    self.biblioteca.head = nuevo_nodo  # Actualizar la cabeza de la lista
                else:
                    prev.next = nuevo_nodo  # Enlazar el nodo anterior al nuevo nodo
                return True
            prev = current
            current = current.next
        return False





