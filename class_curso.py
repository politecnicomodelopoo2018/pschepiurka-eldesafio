from db import DB


class Curso(object):
    idCurso = None
    codigo = None

    def setID(self, id):
        self.idCurso = id

    def setCurso(self, cod):
        self.codigo = cod

    @staticmethod
    def getCursoID(curs_cod):
        curso_data = DB().run("select idCurso from Curso where codigo = '" + curs_cod + "'")
        id_fetch = curso_data.fetchall()
        if len(id_fetch) == 0:
            return False
        return id_fetch[0]["idCurso"]

    @staticmethod
    def getCursoDB(curs_codigo):
        if type(curs_codigo) is not int:
            curso_data = DB().run("select * from Curso where idCurso = " + str(Curso.getCursoID(curs_codigo)))
            curs_fetch = curso_data.fetchall()
        else:
            curso_data = DB().run("select * from Curso where idCurso = " + str(curs_codigo))
            curs_fetch = curso_data.fetchall()

        if len(curs_fetch) == 0:
            return None
        temp_curs = Curso()
        temp_curs.setID(curs_fetch[0]["idCurso"])
        temp_curs.setCurso(curs_fetch[0]["codigo"])
        return temp_curs

    @staticmethod
    def getListaCurso():
        temp_curs_list = []
        curs_dictionary = DB().run("select * from Curso")
        curs_dictionary_fetch = curs_dictionary.fetchall()

        if len(curs_dictionary_fetch) == 0:
            return temp_curs_list

        for curse in curs_dictionary_fetch:
            temp_curs = Curso()
            temp_curs.setID(curse["idCurso"])
            temp_curs.setCurso(curse["codigo"])
            temp_curs_list.append(temp_curs)

        return temp_curs_list

    def insertCurso(self):
        DB().run("insert into Curso values(%s, '%s')" % ("NULL", self.codigo))

    def actualizarCurso(self):
        DB().run("update Curso set codigo = '" + self.codigo + "' where idCurso = " + str(self.idCurso))

    def eliminarCurso(self):
        DB().run("delete from Curso where idCurso = " + str(self.idCurso))

    def verificarAlumnosCurso(self):
        count = DB().run("select count(*) as cantidad from Alumno where Curso_idCurso = " + str(self.idCurso))
        count_fetch = count.fetchall()
        return count_fetch

    def verificarMateriasCurso(self):
        count = DB().run("select count(*) as cantidad from Materia where Curso_idCurso = " + str(self.idCurso))
        count_fetch = count.fetchall()
        return count_fetch

    @staticmethod
    def selectListaAlumnosCurso(curso):
        from class_alumno import Alumno
        temp_list_students = []
        stud_dict = DB().run("select * from Alumno where Curso_idCurso = " + str(curso.idCurso))
        stud_fetch = stud_dict.fetchall()

        if len(stud_fetch) == 0:
            return temp_list_students

        for student in stud_fetch:
            temp_stud = Alumno()
            temp_stud.setID(student["idAlumno"])
            temp_stud.setNombre(student["nombre"])
            temp_stud.setApellido(student["apellido"])
            temp_stud.fecha_nacimiento = student["fecha_nacimiento"]
            temp_stud.setCurso(Curso.getCursoDB(student["Curso_idCurso"]))

            temp_list_students.append(temp_stud)

        return temp_list_students

    @staticmethod
    def selectListaMateriasCurso(curso):
        from class_materia import Materia
        from class_profesor import Profesor
        temp_list_subject = []
        sub_dict = DB().run("select * from Materia where Curso_idCurso = " + str(curso.idCurso))
        sub_fetch = sub_dict.fetchall()

        if len(sub_fetch) == 0:
            return temp_list_subject

        for subject in sub_fetch:
            temp_sub = Materia()
            temp_sub.setID(subject["idMateria"])
            temp_sub.setNombre(subject["nombre"])
            temp_sub.setProfesor(Profesor().getProfesor(int(subject["Profesor_idProfesor"])))
            temp_sub.setCurso(Curso().getCursoDB(subject["Curso_idCurso"]))

            temp_list_subject.append(temp_sub)

        return temp_list_subject
