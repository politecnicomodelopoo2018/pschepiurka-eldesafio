from db import DB

class Familia(object):
    idFamilia = None
    nombre = None

    def setID(self, id):
        self.idFamilia = id

    def setNombre(self, nom):
        self.nombre = nom

    @staticmethod
    def getFamilia(idFamilia):
        family = DB().run('select * from Familia where idFamilia = ' + str(idFamilia))
        fam_fetch = family.fetchall()

        temp_fam = Familia()
        temp_fam.setID(fam_fetch[0]['idFamilia'])
        temp_fam.setNombre(fam_fetch[0]['nombre'])

        return temp_fam

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