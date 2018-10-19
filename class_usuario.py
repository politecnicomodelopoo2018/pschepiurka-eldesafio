from class_familia import Familia
from class_profesor import Profesor
from db import DB
import hashlib

# HASH SHA256


class Usuario(object):
    idUsuario = None
    tipoUsuario = None
    usuario = None
    contraseña = None

    def setID(self, id):
        self.idUsuario = id

    def setTipoUsuario(self, tipoU):
        self.tipoUsuario = tipoU

    def setUsuario(self, user):
        self.usuario = user

    def setContraseña(self, passwd):
        self.contraseña = passwd

    @staticmethod
    def verificarUsuario(user, passwd):
        temp_user = DB().run("select * from Usuario where usuario = '" + user + "'")
        temp_fetch = temp_user.fetchall()
        if temp_fetch[0]["contraseña"] == str(hashlib.sha256(passwd.encode('utf-8')).hexdigest()):
            return True

        return False

    @staticmethod
    def getUsuario(user):
        usuario = DB().run("select * from Usuario where Usuario = '" + user + "'")
        usu_fetch = usuario.fetchall()

        if usu_fetch[0]["idFamilia"] is None and usu_fetch[0]['idProfesor'] is None:
            temp_user = Usuario()
            temp_user.setID(usu_fetch[0]["idUsuario"])
            temp_user.setTipoUsuario(usu_fetch[0]["idAdmin"])
            temp_user.setUsuario(usu_fetch[0]["usuario"])
            temp_user.setContraseña(usu_fetch[0]["contraseña"])

            return temp_user

        elif usu_fetch[0]["idFamilia"] is None:
            temp_user = Usuario()
            temp_user.setID(usu_fetch[0]["idUsuario"])
            temp_user.setTipoUsuario(Profesor().getProfesor(int(usu_fetch[0]["idProfesor"])))
            temp_user.setUsuario(usu_fetch[0]['usuario'])
            temp_user.setContraseña(usu_fetch[0]['contraseña'])

            return usu_fetch

        elif usu_fetch[0]["idProfesor"] is None:
            temp_user = Usuario()
            temp_user.setID(usu_fetch[0]["idUsuario"])
            temp_user.setTipoUsuario(Familia().getFamilia(usu_fetch[0]['idFamilia']))
            temp_user.setUsuario(usu_fetch[0]['usuario'])
            temp_user.setContraseña(usu_fetch[0]['contraseña'])

            return temp_user

        return False

    def insertarUsuarioFamilia(self):
        DB().run("insert into Usuario values(NULL, "
                 + str(self.tipoUsuario.idFamilia) +
                 ", NULL, 0, '"
                 + self.usuario + "', '" +
                 str(hashlib.sha256(self.contraseña.encode('utf-8')).hexdigest()) + "')")

    def insertarUsuarioProfesor(self):
        DB().run("insert into Usuario values(NULL, NULL, "
                 + str(self.tipoUsuario.idProfesor) + ", 0, '"
                 + self.usuario + "', '" +
                 str(hashlib.sha256(self.contraseña.encode('utf-8')).hexdigest()) + "')")

    def insertarUsuarioAdmin(self):
        DB().run("insert into Usuario values(NULL, NULL, NULL, 1, '"
                 + self.usuario + "', '" +
                 str(hashlib.sha256(self.contraseña.encode('utf-8')).hexdigest()) + "')")

    def modificarUsuario(self):
        DB().run("update Usuario set usuario = '" + self.usuario +
                 "', contraseña = '" + self.contraseña +
                 "' where idUsuario = " + str(self.idUsuario))

    def eliminarUsuario(self):
        DB().run("delete from Usuario where idUsuario = " + str(self.idUsuario))
