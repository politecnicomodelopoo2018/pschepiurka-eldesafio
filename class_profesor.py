from class_persona import Persona
from db import DB


class Profesor(Persona):
    def insertProfesor(self):
        DB().run("insert into Profesor values(NULL, '" +
                 self.nombre + "', '" +
                 self.apellido + "', '" +
                 str(self.fecha_nacimiento) + "')")

    def actualizarProfesor(self):
        DB().run("update Profesor set nombre = '" + self.nombre +
               "', apellido = '" + self.apellido +
               "', fecha_nacimiento = '" + str(self.fecha_nacimiento) +
               "' where idProfesor = " + str(self.idPersona))

    def eliminarProfesor(self):
        DB().run("delete from Profesor where idProfesor = " + str(self.idPersona))

    def verificarProfesor(self):
        count_mat = DB().run("select count(*) as cantidad_materias from Materia where Profesor_idProfesor = " + str(self.idPersona))
        count_fetch = count_mat.fetchall()
        return count_fetch

    @staticmethod
    def getListaProfesor():
        temp_teacher_list = []
        teacher_dictionary = DB().run("select * from Profesor")
        for teacher in teacher_dictionary:
            temp_teach = Profesor()
            temp_teach.setID(teacher["idProfesor"])
            temp_teach.setNombre(teacher["nombre"])
            temp_teach.setApellido(teacher["apellido"])

            fecha_nac = str(teacher["fecha_nacimiento"]).split("-", 2)
            temp_teach.setFechaNac(int(fecha_nac[0]), int(fecha_nac[1]), int(fecha_nac[2]))

            temp_teacher_list.append(temp_teach)

        return temp_teacher_list

    @staticmethod
    def getProfesorID(nom, apell):
        id_teacher = DB().run("select idProfesor from Profesor where nombre = '" + nom + "' and apellido = '" + apell + "'")
        id_fetch = id_teacher.fetchall()
        if len(id_fetch) == 0:
            return False
        else:
            return id_fetch[0]["idProfesor"]

    @staticmethod
    def getProfesor(id_profesor):
        if type(id_profesor) is not int:
            split_name = id_profesor.split(" ", 1)
            teach_dict = DB().run("select * from Profesor where idProfesor = " + str(Profesor.getProfesorID(split_name[0], split_name[1])))
            teach_fetch = teach_dict.fetchall()
        else:
            teach_dict = DB().run("select * from Profesor where idProfesor = " + str(id_profesor))
            teach_fetch = teach_dict.fetchall()

        if len(teach_fetch) == 0:
            return False
        else:
            temp_teach = Profesor()
            temp_teach.setID(teach_fetch[0]["idProfesor"])
            temp_teach.setNombre(teach_fetch[0]["nombre"])
            temp_teach.setApellido(teach_fetch[0]["apellido"])

            fecha_nac = str(teach_fetch[0]["fecha_nacimiento"]).split("-", 2)
            temp_teach.setFechaNac(int(fecha_nac[0]), int(fecha_nac[1]), int(fecha_nac[2]))

        return temp_teach