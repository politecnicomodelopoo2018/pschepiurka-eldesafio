from class_persona import Persona
from db import DB
from class_curso import Curso


class Alumno(Persona):
    curso = None

    def setCurso(self, curso):
        self.curso = curso

    def insertAlumno(self):
        DB().run("insert into Alumno values(NULL, '%s', '%s', '%s', %i)"
                 % (self.nombre, self.apellido, str(self.fecha_nacimiento), self.curso.idCurso))

    def actualizarAlumno(self):
        DB().run("update Alumno set nombre = '" + self.nombre +
                 "', apellido = '" + self.apellido +
                 "', fecha_nacimiento = '" + str(self.fecha_nacimiento) +
                 "', Curso_idCurso = " + str(self.curso.idCurso)
                 + " where idAlumno = " + str(self.idPersona) + ";")

    @staticmethod
    def selectListaAlumnos():
        temp_students_list = []
        students_dictionary = DB().run("select * from Alumno")
        for student in students_dictionary:
            temp_student = Alumno()
            temp_student.setID(student["idAlumno"])
            temp_student.setNombre(student["nombre"])
            temp_student.setApellido(student["apellido"])

            fecha_nac = str(student["fecha_nacimiento"]).split("-", 2)
            temp_student.setFechaNac(int(fecha_nac[0]), int(fecha_nac[1]), int(fecha_nac[2]))

            temp_student.setCurso(Curso.getCursoDB(student["Curso_idCurso"]))
            temp_students_list.append(temp_student)

        return temp_students_list

    @staticmethod
    def getAlumnoID(nom, apell):
        student_data = DB().run("select * from Alumno where nombre = '" + nom + "', apell = '" + apell + "'")
        student_fetch = student_data.fetchall()
        if len(student_fetch) == 0:
            return False
        return student_fetch[0]["idAlumno"]

    @staticmethod
    def getAlumno(id):
        if type(id) is not int:
            split_name = id.split(" ", 1)
            students_dictionary = DB().run("select * from Alumno where idAlumno = " + Alumno().getAlumnoID(split_name[0], split_name[1]))
            students_fetch = students_dictionary.fetchall()
        else:
            students_dictionary = DB().run("select * from Alumno where idAlumno = " + str(id))
            students_fetch = students_dictionary.fetchall()

        if len(students_fetch) == 0:
            return False
        else:
            for student in students_fetch:
                temp_alum = Alumno()
                temp_alum.setID(student["idAlumno"])
                temp_alum.setNombre(student["nombre"])
                temp_alum.setApellido(student["apellido"])
                temp_alum.setCurso(Curso().getCursoDB(student["Curso_idCurso"]))

                #fecha_spliteada = str(student)

                temp_alum.fecha_nacimiento = student["fecha_nacimiento"]
            return temp_alum

    def borrarAlumno(self):
        DB().run("delete from Alumno where idAlumno = " + str(self.idPersona))