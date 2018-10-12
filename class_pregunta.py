from db import DB
from random import randint


class Pregunta(object):
    idPregunta = None
    pregunta = None
    respuesta = None

    def setID(self, id):
        self.idPregunta = id

    def setPregunta(self, pregunta):
        self.pregunta = pregunta

    def setRespuesta(self, respuesta):
        self.respuesta = respuesta

    def insertPregunta(self):
        DB().run("insert into Pregunta_Seguridad values(NULL, '" + self.pregunta + "', '" + self.respuesta + "')")

    def updatePregunta(self):
        DB().run("update Pregunta_Seguridad set pregunta = '" + self.pregunta +
                 "', respuesta = '" + self.respuesta +
                 "' where idPregunta = " + str(self.idPregunta))

    def deletePregunta(self):
        DB().run("delete from Pregunta_Seguridad where idPregunta = " + str(self.idPregunta))

    @staticmethod
    def getCantPreguntas():
        cant_preguntas = DB().run("select count(*) from Pregunta_Seguridad")
        cant_fetch = cant_preguntas.fetchall()

        return len(cant_fetch)

    @staticmethod
    def getPreguntaRandom():
        cant_preg = Pregunta().getCantPreguntas()
        idPreg = randint(1, cant_preg)

        preg = DB().run('select * from Pregunta_Seguridad where idPregunta = ' + str(idPreg))
        preg_fetch = preg.fetchall()

        temp_preg = Pregunta()
        temp_preg.setID(preg_fetch[0]['idPregunta'])
        temp_preg.setPregunta(preg_fetch[0]['pregunta'])
        temp_preg.setRespuesta(preg_fetch[0]['respuesta'])

        return temp_preg

    @staticmethod
    def getPregunta(idPreg):
        preg = DB().run("select * from Pregunta where idPregunta = " + str(idPreg))
        preg_fetch = preg.fetchall()

        temp_preg = Pregunta()
        temp_preg.setID(preg_fetch[0]['idPregunta'])
        temp_preg.setPregunta(preg_fetch[0]['pregunta'])
        temp_preg.setRespuesta(preg_fetch[0]['respuesta'])

        return temp_preg
