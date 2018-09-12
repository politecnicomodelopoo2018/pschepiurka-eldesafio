from flask import *
from class_alumno import Alumno
from class_curso import Curso
from class_profesor import Profesor
from class_materia import Materia


app = Flask(__name__)


@app.route('/home')
def opcion():
    return render_template("opcion.html")


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
    curso.eliminarCurso()
    return redirect("/curso/mostrar")


# ALUMNO


@app.route("/alumno/")
def alumno():
    return render_template("/alumno/alumno.html")


# CREAR ALUMNO

@app.route("/alumno/crearAlumno/")
def crearAlumno():
    lista_cursos = Curso.getListaCurso()
    return render_template('/alumno/crearAlumno.html', lista_cursos=lista_cursos)


@app.route("/alumno/crear/", methods=['POST'])
def crearA():
    nombre = request.form["nom"]
    apellido = request.form["apell"]
    fecha_nacimiento = request.form["fn"]
    curso = Curso.getCursoDB(request.form['curs'])

    alumno = Alumno()
    alumno.setNombre(nombre)
    alumno.setApellido(apellido)

    fn_split = str(fecha_nacimiento).split('/', 2)
    alumno.setFechaNac(int(fn_split[2]), int(fn_split[1]), int(fn_split[0]))

    alumno.setCurso(curso)

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
    profesor.eliminarProfesor()
    return redirect('/profesor/mostrar/')


if __name__ == '__main__':
    app.run(debug=True)
