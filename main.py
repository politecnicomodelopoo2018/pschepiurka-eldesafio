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


@app.route('/curso/modificar/')
def modificarCurso():
    return render_template("curso/modificar.html")


@app.route('/curso/modificarCurso/')
def modificar():
    pass


if __name__ == '__main__':
    app.run(debug=True)
