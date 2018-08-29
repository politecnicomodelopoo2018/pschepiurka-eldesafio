from db import DB
from class_profesor import Profesor
from class_curso import Curso


class Materia(object):
    idMateria = None
    nombre = None
    profesor = None
    curso = None

    def setID(self, id):
        self.idMateria = id

    def setNombre(self, nom):
        self.nombre = nom

    def setProfesor(self, prof):
        self.profesor = prof

    def setCurso(self, curs):
        self.curso = curs

    def insertarMateria(self):
        DB().run("insert into Materia values(NULL, '" +
                 self.nombre + "', " +
                 str(self.profesor.idPersona) + ", " +
                 str(self.curso.idCurso) + ")")

    def actualizarMateria(self):
        DB().run("update Materia set nombre = '" + self.nombre +
                 "', Profesor_idProfesor = " + str(self.profesor.idPersona) +
                 ", Curso_idCurso = " + str(self.curso.idCurso) +
                 " where idMateria = " + str(self.idMateria))

    def borrarMateria(self):
        DB().run("delete from Materia where idMateria = " + str(self.idMateria))

    @staticmethod
    def selectListaMaterias():
        temp_subject_list = []
        subject_dict = DB().run("select * from Materia")
        for subject in subject_dict:
            temp_subject = Materia()
            temp_subject.setID(subject["idMateria"])
            temp_subject.setNombre(subject["nombre"])
            temp_subject.setProfesor(Profesor().getProfesor(subject["Profesor_idProfesor"]))
            temp_subject.setCurso(Curso().getCursoDB(subject["Curso_idCurso"]))

            temp_subject_list.append(temp_subject)

        return temp_subject_list

    @staticmethod
    def selectMateria(id_materia):
        subject_dict = DB().run("select * from Materia where idMateria = " + id_materia)
        subject_fetch = subject_dict.fetchall()

        if len(subject_fetch) == 0:
            return False
        else:
            temp_sub = Materia()
            temp_sub.setID(subject_fetch[0]["idMateria"])
            temp_sub.setNombre(subject_fetch[0]["nombre"])
            temp_sub.setProfesor(Profesor().getProfesor(subject_fetch[0]["Profesor_idProfesor"]))
            temp_sub.setCurso(Curso().getCursoDB(subject_fetch[0]["Curso_idCurso"]))

            return temp_sub