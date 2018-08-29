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
            return False
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
            return False

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

    def verificarCurso(self):
        count = DB().run("select count(*) as cantidad from Alumno where Curso_idCurso = " + str(self.idCurso))
        count_fetch = count.fetchall()
        return count_fetch