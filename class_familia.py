from db import DB

class Familia(object):
    idFamilia = None
    nombre = None
    usuario = None
    contraseña = None

    def setID(self, id):
        self.idFamilia = id

    def setNombre(self, nom):
        self.nombre = nom

    def setUsuario(self, user):
        self.usuario = user

    def setContraseña(self, passwd):
        self.contraseña = passwd


    def insertFamilia(self):
        DB().run("insert into Familia values(NULL, '"
                 + self.nombre + "', '"
                 + self.usuario + "', '"
                 + self.contraseña + "')")

    def updateFamilia(self):
        DB().run("update Familia set nombre = '" + self.nombre +
                 "', usuario = '" + self.usuario +
                 "', contraseña = '" + self.contraseña +
                 "' where idFamilia = " + str(self.idFamilia))

    def deleteFamilia(self):
        DB().run("delete from Familia where idFamilia = " + str(self.idFamilia))