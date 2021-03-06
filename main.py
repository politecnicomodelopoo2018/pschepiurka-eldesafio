from flask import *
from class_alumno import Alumno
from class_curso import Curso
from class_profesor import Profesor
from class_materia import Materia
from class_pregunta import Pregunta
from class_nota import Nota
from class_familia import Familia
from class_usuario import Usuario


app = Flask(__name__)
app.secret_key = 'alumnoipm'


# LOGIN


def Session():
    if not 'idUser' in session:
        session['idUser'] = session.get('idUser')


# REGISTROS

# ADMIN #

@app.route('/signup/admin/')
def signupAdmin():
    pregunta_random = Pregunta().getPreguntaRandom()
    return render_template('/login_templates/admin_signup.html', pregunta_random=pregunta_random, signup_ver=None)


@app.route('/signup/admin/verificacion', methods=["POST"])
def verifAdmin():
    pregunta = Pregunta().getPregunta(int(request.form['idPregunta']))
    user = request.form['user']
    passwd = request.form['passwd']
    respuesta = request.form['respuesta']

    if respuesta == pregunta.respuesta:
        temp_user = Usuario()
        temp_user.setUsuario(user)
        temp_user.setContraseña(passwd)

        temp_user.insertarUsuarioAdmin()

        return redirect('/home')

    else:
        pregunta_random = Pregunta().getPreguntaRandom()
        return render_template("/login_templates/admin_signup.html", pregunta_random=pregunta_random, signup_ver=False)

# PROFESOR


@app.route('/signup/profesor/')
def signupProfesor():
    error = False
    return render_template("/login_templates/profesor/profesor_signup.html", error=error)

@app.route('/signup/profesor/crear', methods=["POST"])
def crearUsuarioProfesor():
    nombre_completo = request.form["fullname"]
    usuario = request.form["user"]
    contraseña = request.form["passwd"]

    temp_prof = Profesor().getProfesor(nombre_completo)
    if temp_prof == False:
        return render_template("/login_templates/profesor/profesor_signup.html", error=True)

    else:
        redirect("/home")


# LOGIN
# ADMIN #

@app.route('/login/adminLogin', methods=["POST", "GET"])
def adminLogin():
    if 'user' in request.form:
        usuario = request.form[0]['user']
        return render_template('/login_templates/admin_login.html', user=usuario)
    return render_template('/login_templates/admin_login.html', usuarioAnterior=None)


@app.route('/login/verificacion', methods=["POST"])
def verificacion():
    usuario = request.form['user']
    contraseña = request.form['passwd']
    if Usuario().verificarUsuario(usuario, contraseña) is False:
        return render_template('/login_templates/admin_login.html', usuarioAnterior=usuario)
    else:
        user = Usuario().getUsuario(usuario)
        if user.tipoUsuario == 1:
            if not 'userid' in session:
                session['userid'] = user.idUsuario
            return redirect('/home')



# PROFESOR #
# FAMILIA #

# LOGOUT


@app.route("/logout/")
def logout():
    if 'userid' in session:
        session.pop('userid', None)
    return redirect("/login/adminLogin")

# MAIN PAGE


@app.route('/home/')
def opcion():
    if not 'userid' in session:
        return redirect('/login/adminLogin')

    user = Usuario().getUsuario(int(session['userid']))

    if type(user.tipoUsuario) is Profesor():
        return render_template("opcion.html", user=user, ver="Es Profesor")
    elif type(user.tipoUsuario) is Familia():
        return render_template("opcion.html", user=user, ver="Es Familia")
    elif user.tipoUsuario == 1:
        return render_template("opcion.html", user=user, ver="Es Admin")


# CURSO


@app.route('/curso/')
def curso():
    return render_template("curso/curso.html")


# CREAR CURSO


@app.route('/curso/crear/')
def crearCurso():
    return render_template("curso/crearCurso.html")


@app.route('/curso/crearCurso/', methods=['POST', 'GET'])
def crear():
    codigo = request.form['codigo']
    curso = Curso()
    curso.setCurso(codigo)
    curso.insertCurso()
    return redirect('/curso/')


# MOSTRAR CURSO


@app.route('/curso/mostrar/', methods=['POST', 'GET'])
def seleccionarCurso():
    lista_cursos = Curso.getListaCurso()
    return render_template("curso/mostrarCurso.html", lista_cursos=lista_cursos)


# MODIFICAR CURSO


@app.route('/curso/modificarCurso/', methods=['POST', 'GET'])
def modificarC():
    idCurso = int(request.args.get("id"))
    curso = Curso.getCursoDB(idCurso)
    return render_template("curso/modificacionCurso.html", curso=curso)


@app.route('/curso/modificado/', methods=['POST'])
def modificadoC():
    idCurso = request.form["id"]
    new_cod = request.form["codigo"]
    curso = Curso.getCursoDB(int(idCurso))
    curso.setCurso(new_cod)
    curso.actualizarCurso()
    return redirect("/curso/mostrar")


# ELIMINAR CURSO


@app.route('/curso/eliminarCurso/')
def eliminarCurso():
    idCurso = int(request.args.get("id"))
    curso = Curso.getCursoDB(idCurso)
    ver_alum_curso = curso.verificarAlumnosCurso()
    ver_mat_curso = curso.verificarMateriasCurso()
    if ver_alum_curso[0]['cantidad'] > 0 or ver_mat_curso[0]['cantidad'] > 0:
        lista_alumnos_curso = Curso.selectListaAlumnosCurso(curso)
        lista_materias_curso = Curso.selectListaMateriasCurso(curso)
        return render_template("/curso/errorEliminarCurso.html", lista_alumnos_curso=lista_alumnos_curso,
                               lista_materias_curso=lista_materias_curso)
    curso.eliminarCurso()
    return redirect("/curso/mostrar")


# MOSTRAR ALUMNOS DE X CURSO


@app.route('/curso/mostrarAlumnos/')
def mostrarAlumnosCurso():
    lista_cursos = Curso().getListaCurso()
    return render_template("/curso/mostrarAlumnos.html", lista_cursos=lista_cursos)


@app.route('/curso/alumnosCurso/', methods=["POST"])
def alumnosCurso():
    idCurso = request.form["idCurso"]
    curso = Curso().getCursoDB(int(idCurso))
    lista_cursos = Curso().getListaCurso()
    lista_alumnos_curso = Curso().selectListaAlumnosCurso(curso)
    return render_template("/curso/alumnosCurso.html", lista_alumnos_curso=lista_alumnos_curso, lista_cursos=lista_cursos, idCursoAnterior=int(idCurso))


# FAMILIA

@app.route("/familia/")
def familia():
    return render_template("/familia/familia.html")


@app.route("/familia/mostrar/")
def mostrarFamilia():
    lista_familia = Familia().selectListaFamilia()
    return render_template("/familia/mostrarFamilia.html", lista_familia=lista_familia)


# CREAR FAMILIA


@app.route("/familia/crearFamilia/")
def crearFamilia():
    return render_template("/familia/crearFamilia.html")


@app.route("/familia/crearF/", methods=["POST"])
def crearF():
    nombre_familia = request.form["n_familia"]

    temp_familia = Familia()
    temp_familia.setNombre(nombre_familia)
    temp_familia.insertFamilia()

    return redirect("/familia/")


# MODIFICAR FAMILIA


@app.route("/familia/modificarFamilia/", methods=["GET"])
def modificarFamilia():
    idFamilia = int(request.args.get("id"))
    temp_fam = Familia().getFamilia(idFamilia)
    return render_template("/familia/modificarFamilia.html", temp_fam=temp_fam)


@app.route("/familia/modificarF/", methods=["POST", "GET"])
def modificarF():
    idFamilia = int(request.form.get("id"))
    new_nombre = request.form["nombreFam"]
    temp_fam = Familia().getFamilia(idFamilia)

    temp_fam.setNombre(new_nombre)
    temp_fam.updateFamilia()

    return redirect("/familia/mostrar/")


# ELIMINAR FAMILIA


@app.route("/familia/eliminarFamilia/", methods=["POST", "GET"])
def eliminarFamilia():
    id = request.args.get("id")
    temp_fam = Familia().getFamilia(id)

    temp_fam.deleteFamilia()
    return redirect("/familia/mostrar")


# ALUMNO


@app.route("/alumno/")
def alumno():
    return render_template("/alumno/alumno.html")


# CREAR ALUMNO

@app.route("/alumno/crearAlumno/")
def crearAlumno():
    lista_cursos = Curso.getListaCurso()
    lista_familias = Familia().selectListaFamilia()
    return render_template('/alumno/crearAlumno.html', lista_cursos=lista_cursos, lista_familias=lista_familias)


@app.route("/alumno/crear/", methods=['POST'])
def crearA():
    nombre = request.form["nom"]
    apellido = request.form["apell"]
    fecha_nacimiento = request.form["fn"]
    curso = Curso.getCursoDB(request.form['curs'])
    familia = Familia.getFamilia(request.form['fam'])

    alumno = Alumno()
    alumno.setNombre(nombre)
    alumno.setApellido(apellido)

    fn_split = str(fecha_nacimiento).split('-', 2)
    alumno.setFechaNac(int(fn_split[0]), int(fn_split[1]), int(fn_split[2]))

    alumno.setCurso(curso)
    alumno.setFamilia(familia)

    alumno.insertAlumno()
    return redirect('/alumno/')

# MOSTRAR ALUMNO


@app.route('/alumno/mostrar/')
def mostrarAlumno():
    lista_alumnos = Alumno.selectListaAlumnos()
    lista_cursos = Curso.getListaCurso()
    return render_template('/alumno/mostrarAlumno.html', lista_alumnos=lista_alumnos, ver_curso=len(lista_cursos))


# MODIFICAR ALUMNO


@app.route('/alumno/modificarAlumno/', methods=['POST', 'GET'])
def modificarAlumno():
    idAlumno = int(request.args.get('id'))
    alumno = Alumno().getAlumno(idAlumno)
    lista_cursos = Curso.getListaCurso()
    return render_template('/alumno/modificarAlumno.html', alumno=alumno, lista_cursos=lista_cursos)


@app.route('/alumno/modificar/', methods=['POST', 'GET'])
def modificarA():
    id = request.form['id']
    nom = request.form['nom']
    apell = request.form['apell']
    fn = request.form['fn']
    curs = request.form['curs']

    alumno = Alumno().getAlumno(int(id))
    if nom != alumno.nombre:
        alumno.setNombre(nom)
    if apell != alumno.apellido:
        alumno.setApellido(apell)
    if fn != alumno.fecha_nacimiento:
        fn_split = fn.split('-', 2)
        alumno.setFechaNac(int(fn_split[0]), int(fn_split[1]), int(fn_split[2]))
    if curs != alumno.curso:
        curso = Curso().getCursoDB(curs)
        alumno.setCurso(curso)

    alumno.actualizarAlumno()
    return redirect('/alumno/mostrar/')


# ELIMINAR ALUMNO


@app.route('/alumno/eliminarAlumno/', methods=['GET'])
def eliminarAlumno():
    id = request.args.get('id')
    alumno = Alumno().getAlumno(int(id))
    alumno.borrarAlumno()
    return redirect('/alumno/mostrar')


# PROFESOR


@app.route('/profesor/')
def profesor():
    return render_template('/profesor/profesor.html')


# CREAR PROFESOR


@app.route('/profesor/crearProfesor/')
def crearProfesor():
    return render_template('/profesor/crearProfesor.html')


@app.route('/profesor/crear/', methods=["POST"])
def crearP():
    nombre = request.form['nom']
    apellido = request.form['apell']
    fn = request.form['fn']

    profesor = Profesor()
    profesor.setNombre(nombre)
    profesor.setApellido(apellido)
    fn_split = fn.split('-', 2)
    profesor.setFechaNac(int(fn_split[0]), int(fn_split[1]), int(fn_split[2]))

    profesor.insertProfesor()
    return redirect('/profesor/')


# MOSTRAR PROFESOR


@app.route('/profesor/mostrar/')
def mostrarProfesor():
    lista_profesores = Profesor.getListaProfesor()
    return render_template('/profesor/mostrarProfesor.html', lista_profesores=lista_profesores)


# MODIFICAR PROFESOR


@app.route('/profesor/modificarProfesor/', methods=['GET'])
def modificarProfesor():
    idProfesor = request.args.get('id')
    profesor = Profesor.getProfesor(int(idProfesor))
    return render_template('/profesor/modificarProfesor.html', profesor=profesor)


@app.route('/profesor/modificar/', methods=['POST'])
def modificarP():
    idProfesor = request.form['id']
    nom = request.form['nom']
    apell = request.form['apell']
    fn = request.form['fn']

    profesor = Profesor.getProfesor(int(idProfesor))
    if nom != profesor.nombre:
        profesor.setNombre(nom)
    if apell != profesor.apellido:
        profesor.setApellido(apell)
    if fn != profesor.fecha_nacimiento:
        fn_split = fn.split('-', 2)
        profesor.setFechaNac(int(fn_split[0]), int(fn_split[1]), int(fn_split[2]))

    profesor.actualizarProfesor()
    return redirect('/profesor/mostrar/')


# ELIMINAR PROFESOR


@app.route('/profesor/eliminarProfesor/', methods=['GET'])
def eliminarProfesor():
    id = request.args.get('id')
    profesor = Profesor.getProfesor(int(id))
    verif_materias = profesor.verificarMateriasProfesor()
    if verif_materias[0]['cantidad'] > 0:
        lista_materias_profesor = Profesor().selectMateriasProfesor(profesor)
        return render_template('/profesor/errorEliminarProfesor.html', lista_materias_profesor=lista_materias_profesor)
    profesor.eliminarProfesor()
    return redirect('/profesor/mostrar/')


# MATERIA


@app.route('/materia/')
def materia():
    return render_template('/materia/materia.html')


# CREAR MATERIA


@app.route('/materia/crearMateria/')
def crearMateria():
    lista_curso = Curso().getListaCurso()
    lista_profesores = Profesor().getListaProfesor()
    return render_template('/materia/crearMateria.html', lista_curso=lista_curso, lista_profesores=lista_profesores)


@app.route('/materia/crear/', methods=["POST"])
def crearC():
    nom = request.form['nom']
    curs = Curso().getCursoDB(request.form['curs'])
    prof = Profesor().getProfesor(int(request.form['prof']))

    materia = Materia()
    materia.setNombre(nom)
    materia.setCurso(curs)
    materia.setProfesor(prof)
    materia.insertarMateria()
    return redirect('/materia/')


# MOSTRAR MATERIA


@app.route('/materia/mostrar/')
def mostrarMateria():
    lista_materias = Materia().selectListaMaterias()
    url = "/pepito/pepe/pepe.exe"
    return render_template('/materia/mostrarMateria.html', lista_materias=lista_materias, url=url)


# MODIFICAR MATERIA


@app.route('/materia/modificarMateria/')
def modificarMateria():
    idMat = request.args.get('id')
    materia = Materia().selectMateria(idMat)
    lista_curso = Curso().getListaCurso()
    lista_profesores = Profesor().getListaProfesor()
    return render_template('/materia/modificarMateria.html', materia=materia, lista_curso=lista_curso, lista_profesores=lista_profesores)


@app.route('/materia/modificar/', methods=["POST"])
def modificar():
    idMateria = request.form['id']
    nom = request.form['nom']
    curs = Curso().getCursoDB(request.form['curs'])
    prof = Profesor().getProfesor(int(request.form['prof']))

    materia = Materia().selectMateria(idMateria)
    if nom != materia.nombre:
        materia.setNombre(nom)
    if curs != materia.curso:
        materia.setCurso(curs)
    if prof != materia.profesor:
        materia.setProfesor(prof)

    materia.actualizarMateria()
    return redirect('/materia/mostrar/')


@app.route('/materia/eliminarMateria/', methods=["GET"])
def eliminarMateria():
    id = request.args.get('id')
    materia = Materia.selectMateria(id)

    materia.borrarMateria()
    return redirect('/materia/mostrar')


if __name__ == '__main__':
    app.run(debug=True)