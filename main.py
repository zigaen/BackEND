from flask import Flask, render_template, request, make_response
import datetime
import random

app = Flask(__name__)


@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year
    current_hour = datetime.datetime.now().hour
    cities = ["Boston", "Vienna", "Paris", "Berlin"]
    user_name = request.cookies.get("user_name")

    return render_template("index.html", some_text=some_text, current_year=current_year, current_hour=current_hour, cities=cities, name=user_name)


@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response

@app.route("/guess", methods=["GET", "POST"])
def guess():
    return render_template("guess.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/boogle")
def boogle():
    return render_template("boogle.html")

@app.route("/base")
def base():
    return render_template("base.html")



if __name__ == '__main__':
    app.run()