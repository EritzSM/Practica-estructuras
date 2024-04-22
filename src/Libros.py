class Libro:
    def __init__(self, numero_libro, genero, autor, titulo, ano_publicacion, tarifa_diaria):
        self.numero_libro = numero_libro
        self.genero = genero
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacion = ano_publicacion
        self.tarifa_diaria = tarifa_diaria
        self.disponible = True

    def __str__(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Número de Libro: {self.numero_libro}, Género: {self.genero}, Autor: {self.autor}, Título: {self.titulo}, Año de Publicación: {self.ano_publicacion}, Tarifa Diaria de Alquiler: {self.tarifa_diaria}, Disponibilidad: {disponibilidad}"


class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        curr_node = self.head
        while curr_node is not None:
            yield curr_node
            curr_node = curr_node.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node





