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


    def historial_prestamos_usuario(self, id_usuario):
            usuario = None
            for u in self.usuarios:
                if u.id_usuario == id_usuario:
                    usuario = u
                    break
            if usuario is None:
                input("Usuario no encontrado.")
                return
            input(f"Historial de préstamos de {usuario.nombre}:")
            for prestamo in usuario.historial_prestamos:
                fecha_devolucion_str = prestamo.fecha_devolucion.strftime('%Y-%m-%d') if prestamo.fecha_devolucion else 'N/A'
                input(f"Libro: {prestamo.libro.titulo}, Fecha de préstamo: {prestamo.fecha_prestamo.strftime('%Y-%m-%d')}, Fecha de devolución: {fecha_devolucion_str}")




    def mostrar_libros_disponibles(self):
        os.system('cls')
        print(f'''          -LIBROS DISPONIBLES-''' '\n' '\n')
        self.catalogo.consultar_libros_disponibles()
        input("Presiona Enter para volver al menú principal...")

    def realizar_prestamo(self):
        os.system('cls')
        print(f'''          -REALIZAR PRESTAMO-''' '\n' '\n')
        id_libro = int(input("Ingrese el ID del libro a prestar: "))
        id_usuario = int(input("Ingrese el ID del usuario: "))
        fecha_prestamo = input("Ingrese la fecha de préstamo (YYYY-MM-DD): ")
        fecha_prestamo_obj = datetime.strptime(fecha_prestamo, '%Y-%m-%d')
        self.catalogo.prestar_libro(id_libro, id_usuario, fecha_prestamo_obj) 

    def realizar_devolucion(self):
        os.system('cls')
        print(f'''          -REALIZAR DEVOLUCION-''' '\n' '\n')
        id_libro = int(input("Ingrese el ID del libro a devolver: "))
        id_usuario = int(input("Ingrese el ID del usuario: "))
        fecha_devolucion = input("Ingrese la fecha de devolución (YYYY-MM-DD): ")
        fecha_devolucion_obj = datetime.strptime(fecha_devolucion, '%Y-%m-%d')
        self.catalogo.devolver_libro(id_libro, id_usuario, fecha_devolucion_obj)

    def historial_prestamos_usuario(self):
        os.system('cls')
        print(f'''          -HISTORIAL PRESTAMOS USUARIO-''' '\n' '\n')
        id_usuario = int(input("Ingrese el ID del usuario para ver su historial de préstamos: "))
        self.catalogo.historial_prestamos_usuario(id_usuario)


    def agregar_libro(self):
        os.system('cls')
        print(f'''          -AGREGAR LIBRO-''' '\n' '\n')
        id_libro = int(input("Ingrese el ID del libro: "))
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        nuevo_libro = Libro(id_libro, titulo, autor)
        self.catalogo.agregar_libro(nuevo_libro)
        print("Libro agregado al catálogo.")