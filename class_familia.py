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

    @staticmethod
    def selectListaFamilia():
        temp_family_list = []
        family = DB().run('select * from Familia')
        family_fetch = family.fetchall()

        if len(family_fetch) == 0:
            return temp_family_list

        for family in family_fetch:
            temp_family = Familia()
            temp_family.setID(family["idFamilia"])
            temp_family.setNombre(family["nombre"])

            temp_family_list.append(temp_family)

        return temp_family_list

    def getCantidadMiembros(self):
        cant_fam = DB().run("select count(*) as Cantidad from Alumno where Familia_idFamilia = '" + str(self.idFamilia) + "'")
        cant_fetch = cant_fam.fetchall()
        return cant_fetch[0]["Cantidad"]

    def insertFamilia(self):
        DB().run("insert into Familia values(NULL, '"
                 + self.nombre + "')")

    def updateFamilia(self):
        DB().run("update Familia set nombre = '" + self.nombre +
                 "' where idFamilia = " + str(self.idFamilia))

    def deleteFamilia(self):
        DB().run("delete from Familia where idFamilia = " + str(self.idFamilia))