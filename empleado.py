from persona import Persona
class Empleado(Persona):
    def __init__(self, id_empleado, sueldo):
        self._id_empleado = id_empleado
        self._sueldo = sueldo

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, value):
        if isinstance(value, int) and value > 0:
            self._id_empleado = value
        else:
            raise ValueError("El ID del empleado debe ser un entero positivo.")

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._sueldo = value
        else:
            raise ValueError("El sueldo debe ser un número positivo o cero.")

    def __str__(self):
        return f"Empleado[ID: {self._id_empleado}, Sueldo: {self._sueldo}]"

# Ejemplo de uso:
empleado = Empleado(68,1000)
print(empleado)

