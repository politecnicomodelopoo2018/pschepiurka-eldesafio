from class_familia import Familia
from class_profesor import Profesor
from db import DB
import hashlib

# HASH SHA256


class Usuario(object):
    idUsuario = None
    usuario = None
    contraseña = None

    def setID(self, id):
        self.idUsuario = id

    def setUsuario(self, user):
        self.usuario = user

    def setContraseña(self, passwd):
        self.contraseña = passwd

    @staticmethod
    def verificarUsuario(user, passwd):
        temp_user = DB().run("select * from Usuario where usuario = " + user)
        if temp_user[0]["contraseña"] == str(hashlib.sha256(passwd.encode('utf-8')).hexdigest()):
            return True

        return False

    def insertarUsuarioFamilia(self, idFamilia):
        DB().run("insert into Usuario values(NULL, "
                 + str(idFamilia) +
                 ", NULL, 0, '"
                 + self.usuario + "', '" +
                 str(hashlib.sha256(self.contraseña.encode('utf-8')).hexdigest()) + "')")

    def insertarUsuarioProfesor(self, idProfesor):
        DB().run("insert into Usuario values(NULL, NULL, "
                 + idProfesor + ", 0, '"
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
