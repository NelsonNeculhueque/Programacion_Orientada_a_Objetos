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