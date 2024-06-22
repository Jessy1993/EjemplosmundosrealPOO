# Definición de la clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} (ISBN: {self.isbn})"

# Definición de la clase Miembro
class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha prestado {libro}.")
        else:
            print(f"Lo siento, {libro} no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto {libro}.")
        else:
            print(f"{self.nombre} no ha prestado {libro}.")

    def __str__(self):
        return self.nombre

# Definición de la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"{libro} ha sido agregado a la biblioteca.")

    def registrar_miembro(self, miembro):
        self.miembros.append(miembro)
        print(f"{miembro} ha sido registrado como miembro.")

    def mostrar_libros_disponibles(self):
        print("Libros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                print(f" - {libro}")

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Crear y agregar libros a la biblioteca
libro1 = Libro("1984", "George Orwell", "1234567890")
libro2 = Libro("To Kill a Mockingbird", "Harper Lee", "1234567891")
libro3 = Libro("The Great Gatsby", "F. Scott Fitzgerald", "1234567892")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear y registrar miembros
miembro1 = Miembro("Alice")
miembro2 = Miembro("Bob")

biblioteca.registrar_miembro(miembro1)
biblioteca.registrar_miembro(miembro2)

# Prestar y devolver libros
miembro1.prestar_libro(libro1)
miembro2.prestar_libro(libro1)  # Intentar prestar un libro ya prestado
miembro1.devolver_libro(libro1)
miembro2.prestar_libro(libro1)

# Mostrar libros disponibles
biblioteca.mostrar_libros_disponibles()
