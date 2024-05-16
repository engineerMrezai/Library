import flask
from lib_main import Book

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("index.html")


@app.route('/about')
def about():
    return flask.render_template('about.html')


@app.route('/bookslist')
def bookslist():
    return flask.render_template('bookslist.html', books=Book.all())


@app.route('/deletebook', methods=["GET", "POST"])
def deletebook():
    if flask.request.method == "POST":
        temp = flask.request.form
        Book.delete(temp['ISBN'])
        return flask.redirect("/bookslist")
    return flask.render_template('deletebook.html')


@app.route('/newbook', methods=["GET", "POST"])
def addbook():
    if flask.request.method == 'POST':
        temp = dict(flask.request.form)
        Book(temp['ISBN'], temp['title'], temp['author'], temp['price'], temp['page'])
        return flask.redirect('/bookslist')
    return flask.render_template('newbook.html')


app.run()
