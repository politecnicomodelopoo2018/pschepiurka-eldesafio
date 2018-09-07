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
def modificar():
    idCurso = int(request.args.get("id"))
    curso = Curso.getCursoDB(idCurso)
    return render_template("curso/modificacionCurso.html", curso=curso)


@app.route('/curso/modificado/', methods=['POST'])
def modificado():
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
    return render_template('/alumno/crearAlumno.html')


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


if __name__ == '__main__':
    app.run(debug=True)
