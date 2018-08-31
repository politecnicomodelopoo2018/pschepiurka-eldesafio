from flask import *
from class_alumno import Alumno
from class_curso import Curso
from class_profesor import Profesor
from class_materia import Materia


app = Flask(__name__)


@app.route('/home')
def opcion():
    return render_template("opcion.html")


@app.route('/curso/')
def curso():
    return render_template("curso/curso.html")


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


@app.route('/curso/modificar/', methods=['POST', 'GET'])
def seleccionarCurso():
    lista_cursos = Curso.getListaCurso()
    return render_template("curso/modificar.html", lista_cursos=lista_cursos)


@app.route('/curso/modificarCurso/', methods=['POST', 'GET'])
def modificar():
    idCurso = request.args.get("id")
    curso = Curso.getCursoDB(idCurso)
    return render_template("curso/modificacion.html", curso=curso)


@app.route('/curso/modificado/', methods=['POST', 'GET'])
def modificado():
    idCurso = request.form["id"]
    new_cod = request.form["codigo"]
    curso = Curso.getCursoDB(idCurso)
    curso.setCurso(new_cod)
    curso.actualizarCurso()
    return redirect(url_for("modificar"))


if __name__ == '__main__':
    app.run(debug=True)
