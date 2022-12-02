import csv
from persona import Persona

def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """

personas = {}    
archivo = open("personas.csv", "r")
archivo_csv = csv.reader(archivo)
next(archivo_csv)
for nombre, dni, fecha_nacimiento in archivo_csv:
    persona = Persona(dni, nombre, fecha_nacimiento)
    persona.crear_cuenta()

    personas['dni'] = persona

archivo.close()
print(f' {personas}')
return personas
