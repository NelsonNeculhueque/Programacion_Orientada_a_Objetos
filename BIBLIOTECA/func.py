    def agregar_libro(self, libro):
            
            for l in self.libros:
                if l.id_libro == libro.id_libro:
                    input(f"El ID {libro.id_libro} ya está en uso. Elija otro ID.")
                    return

            self.libros.append(libro)
            input("Libro agregado al catálogo.")

    def eliminar_libro(self, id_libro):
        libro_a_eliminar = None
        for libro in self.libros:
            if libro.id_libro == id_libro:
                libro_a_eliminar = libro
                break
        if libro_a_eliminar:
            self.libros.remove(libro_a_eliminar)
            print("Libro eliminado del catálogo.")
        else:
            print("Libro no encontrado en el catálogo.")

    def registrar_usuario(self, usuario):
        for u in self.usuarios:
            if u.id_usuario == usuario.id_usuario:
                input(f"El ID {usuario.id_usuario} ya está en uso. Elija otro ID.")
                return
        self.usuarios.append(usuario)
        input("Usuario registrado.")

    def prestar_libro(self, id_libro, id_usuario, fecha_prestamo):
        libro = None
        usuario = None
        for l in self.libros:
            if l.id_libro == id_libro:
                libro = l
                break
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                usuario = u
                break
        if libro is None or usuario is None:
            input("Libro o usuario no encontrados.")
            return
        if libro.prestado:
            input("El libro ya ha sido prestado.")
        else:
            libro.prestado = True
            prestamo = Prestamo(libro, usuario, fecha_prestamo)
            usuario.historial_prestamos.append(prestamo)
            self.prestamos.append(prestamo)
            input(f"Prestamo realizado: {libro.titulo} a {usuario.nombre}")

    def devolver_libro(self, id_libro, id_usuario, fecha_devolucion):
        libro = None
        usuario = None
        for l in self.libros:
            if l.id_libro == id_libro:
                libro = l
                break
        for u in self.usuarios:
            if u.id_usuario == id_usuario:
                usuario = u
                break
        if libro is None or usuario is None:
            input("Libro o usuario no encontrados.")
            return
        
        libro_prestado = False
        for prestamo in usuario.historial_prestamos:
            if prestamo.libro.id_libro == id_libro and prestamo.fecha_devolucion is None:
                libro_prestado = True
                prestamo.fecha_devolucion = fecha_devolucion
                libro.prestado = False
                input(f"Libro {libro.titulo} devuelto por {usuario.nombre}.")
                break
        if not libro_prestado:
            input("El usuario no tiene prestado este libro.")

    def consultar_libros_disponibles(self):
        input("Libros disponibles:")
        for libro in self.libros:
            if not libro.prestado:
                input(f"ID: {libro.id_libro}, Título: {libro.titulo}, Autor: {libro.autor}")