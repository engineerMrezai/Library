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


app.run()
