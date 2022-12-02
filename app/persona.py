import datetime

from cuenta import Cuenta

def convertir_fecha(string_fecha):
    anio = string_fecha[0:4]
    mes = string_fecha[5:7]
    dia = string_fecha[8:10]
    return datetime.date(int(anio), int(mes), int(dia))

class Persona(object):
    def __init__(self, dni, nombre, str_fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'   

    def crear_cuenta(self):

        cuenta = Cuenta()
        cuenta.crear_movimiento(" Cuenta creada. Se le otorgaron $", 1500)
        self.cuentas.append(cuenta)

    def saludo(self):
        return f"Hola {self.nombre}"        