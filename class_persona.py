import datetime


class Persona(object):
    idPersona = None
    nombre = None
    apellido = None
    fecha_nacimiento = None

    def setID(self, id):
        self.idPersona = id

    def setNombre(self, nom):
        self.nombre = nom

    def setApellido(self, apell):
        self.apellido = apell

    def setFechaNac(self, año, mes, dia):
        self.fecha_nacimiento = datetime.date(año, mes, dia)