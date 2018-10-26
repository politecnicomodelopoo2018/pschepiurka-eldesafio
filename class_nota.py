from db import DB


class Nota(object):
    idNota = None
    materia = None
    alumno = None
    trimestre = None
    nota = None

    def setID(self, id):
        self.idNota = id

    def setMateria(self, materia):
        self.materia = materia

    def setAlumno(self, alumno):
        self.alumno = alumno

    def setTrimestre(self, trim):
        self.trimestre = trim

    def setNota(self, nota):
        self.nota = nota

    def insertNota(self):
        DB().run("insert into Nota values(NULL, "
                 + self.materia.idMateria + ", "
                 + self.alumno.idPersona + ", "
                 + self.trimestre + ", "
                 + self.nota + ")")

    def updateNota(self):
        DB().run("update Nota set idMateria = " + str(self.materia.idMateria) +
                 ", idAlumno = " + str(self.alumno.idPersona) +
                 ", Trimestre = " + self.trimestre +
                 ", Nota = " + self.nota +
                 " where idNota = " + str(self.idNota))

    def deleteNota(self):
        DB().run("delete from Nota where idNota = " + str(self.idNota))
