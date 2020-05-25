from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/boogle")
def boogle():
    return render_template("boogle.html")

if __name__ == '__main__':
    app.run()