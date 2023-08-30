class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

libro1 = Libro(1, "Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro(2, "1984", "George Orwell")
libro3 = Libro(3, "El Hobbit", "J.R.R. Tolkien")
libro4 = Libro(4, "Harry Potter y la piedra filosofal", "J.K. Rowling")
libro5 = Libro(5, "Crimen y castigo", "Fyodor Dostoevsky")


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.historial_prestamos = []

    def __str__(self):
        return f"ID: {self.id_usuario}, Nombre: {self.nombre}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = None

    def __str__(self):
        return f"Libro: {self.libro.titulo}, Usuario: {self.usuario.nombre}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"
