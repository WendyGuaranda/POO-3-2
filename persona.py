class Persona:
    def __init__(self, nombre, genero, edad, direccion):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    # Encapsulamiento de nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Encapsulamiento de genero
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    # Encapsulamiento de edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    # Encapsulamiento de direccion
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    # Representación en cadena de texto
    def __str__(self):
        return f'Nombre: {self.nombre}, Género: {self.genero}, Edad: {self.edad}, Dirección: {self.direccion}'

# Ejemplo de uso
persona = Persona('Mario Mendez', 'Masculino', 45, 'Avenida Delta')
print(persona)
