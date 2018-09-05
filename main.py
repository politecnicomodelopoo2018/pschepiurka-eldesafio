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
    return render_template("curso/crear.html")


@app.route('/curso/crearCurso/', methods=['POST', 'GET'])
def crear():
    if request.method == 'POST':
        codigo = request.form['codigo']
        curso = Curso()
        curso.setCurso(codigo)
        curso.insertCurso()
        return redirect('/home')


# MOSTRAR CURSO


@app.route('/curso/mostrar/', methods=['POST', 'GET'])
def seleccionarCurso():
    lista_cursos = Curso.getListaCurso()
    return render_template("curso/mostrar.html", lista_cursos=lista_cursos)


# MODIFICAR CURSO


@app.route('/curso/modificarCurso/', methods=['POST', 'GET'])
def modificar():
    idCurso = int(request.args.get("id"))
    curso = Curso.getCursoDB(idCurso)
    return render_template("curso/modificacion.html", curso=curso)


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


if __name__ == '__main__':
    app.run(debug=True)
