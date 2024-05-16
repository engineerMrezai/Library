import flask
import lib_db

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/bookslist')
def bookslist():
    return flask.render_template('bookslist.html', books=lib_db.all())


@app.route('/deletebook', methods=["GET", "POST"])
def deletebook():
    if flask.request.method == "POST":
        temp = flask.request.form
        lib_db.delete(temp['ISBN'])
        return flask.redirect("/bookslist")
    return flask.render_template('deletebook.html')


app.run()
