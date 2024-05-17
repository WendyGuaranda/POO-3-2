from empleado import Empleado
class Cliente(Empleado):
    def __init__(self, idCliente, fechaRegistro, vip=False):
        self._idCliente = idCliente
        self._fechaRegistro = fechaRegistro
        self._vip = vip

    @property
    def idCliente(self):
        return self._idCliente

    @idCliente.setter
    def idCliente(self, nuevoNumero):
        self._idCliente = nuevoNumero

    @property
    def fechaRegistro(self):
        return self._fechaRegistro

    @fechaRegistro.setter
    def fechaRegistro(self, nuevaFecha):
        self._fechaRegistro = nuevaFecha

    @property
    def vip(self):
        return self._vip

    @vip.setter
    def vip(self, es_vip):
        self._vip = es_vip

    def __str__(self):
        return f"Cliente {self.idCliente} (Registrado el {self.fechaRegistro}) - {'VIP' if self.vip else 'No VIP'}"

# Ejemplo de uso:
cliente1 = Cliente(idCliente=955, fechaRegistro='2024/01/11', vip=True)
print(str(cliente1))
