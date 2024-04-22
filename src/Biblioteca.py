from Libros import LinkedList, Node
class GestorLibros:
    def __init__(self):
        self.biblioteca = LinkedList()
        self.ingreso_total = 0

    def agregar_libro(self, libro):
        self.biblioteca.append(libro)

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
        current = self.biblioteca.head
        while current:
            if current.value.autor == autor:
                return current.value, "Disponible" if current.value.disponible else "No disponible"
            current = current.next
        return None, "No se encontró el libro"

    def buscar_por_ano_publicacion(self, ano_publicacion):
        current = self.biblioteca.head
        while current:
            if current.value.ano_publicacion == ano_publicacion:
                return current.value, "Disponible" if current.value.disponible else "No disponible"
            current = current.next
        return None, "No se encontró el libro"

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
        libros_disponibles = self.listar_disponibles_por_genero(genero)
        if libros_disponibles:
            for libro in libros_disponibles:
                if libro.disponible:
                    libro.disponible = False
                    return True, libro
            return False, "No hay libros disponibles para alquilar en el género especificado."
        else:
            return False, "No hay libros disponibles en el género especificado."

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

    def calcular_descuento(self):
        total_libros_alquilados = 0
        current = self.biblioteca.head
        while current:
            if not current.value.disponible:
                total_libros_alquilados += 1
            current = current.next
        if total_libros_alquilados >= 2:
            return 0.1  # Descuento del 10% por libro
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





