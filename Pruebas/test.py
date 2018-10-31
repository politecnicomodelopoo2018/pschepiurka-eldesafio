from flask import *
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login')
def login():
    return render_template ("login.html")
@app.route('/esto', methods=['POST', 'GET'])
def esto():
    if request.method == 'POST':
        user = request.form["nm"]
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get("nm")
        return render_template('/success/' + user)


if __name__ == '__main__':
    app.run(debug=True)
