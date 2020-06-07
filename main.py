from flask import Flask, render_template, request, make_response, redirect, url_for
import datetime
import random
from models import User, db

app = Flask(__name__)
db.create_all()  # create (new) tables in the database


@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("user-name")
    email = request.form.get("user-email")

    # create a User object
    user = User(name=name, email=email)

    # save the user object into a database
    db.add(user)
    db.commit()
    response = make_response(redirect(url_for("index")))
    response.set_cookie("email", email)

    return response


@app.route("/")
def index():
    email_address = request.cookies.get("email")
    current_year = datetime.datetime.now().year
    current_hour = datetime.datetime.now().minute
    # get user from the database based on email address
    if email_address:
        user = db.query(User).filter_by(email=email_address).first()
    else:
        user = None

    return render_template("index.html", current_year=current_year, current_hour=current_hour, user=user)


@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        some_number = request.cookies.get("some_number")
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name, number=some_number)
    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")
        some_number = request.form.get("some-number")

        print(contact_name)
        print(contact_email)
        print(contact_message)
        print(some_number)

        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)
        response.set_cookie("some_number", some_number)

        return response


def message_game(number_1_30, secret_number):
    message = ""
    if number_1_30 == secret_number:
        message = "Congratulations, you guessed the number! The secret number was :{0}  PLAY AGAIN! ".format(str(secret_number))
    elif number_1_30 < secret_number:
        message = "Sorry, the number was too small!"
    elif number_1_30 > secret_number:
        message = "Sorry, the number you entered was too big!"
    return message


@app.route("/guess", methods=["GET", "POST"])
def guess():
    secret_number = request.cookies.get("secret_number")
    if request.method == "GET":
        return render_template("guess.html")
    elif request.method == "POST":
        number_1_30 = request.form.get("number_1_30")
        if number_1_30 == "":
            return render_template("guess.html", message="Input number!")
        elif not secret_number:
            secret_number = random.randint(1, 30)
            response = make_response(render_template("guess.html",
                                                     number_1_30=number_1_30,
                                                     message=message_game(int(number_1_30), secret_number)
                                                     ))
            response.set_cookie("number_1_30", str(number_1_30))
            response.set_cookie("secret_number", str(secret_number))
            return response
        else:
            if number_1_30:
                secret_number = int(secret_number)
                response = make_response(render_template("guess.html",
                                                         number_1_30=number_1_30,
                                                         message=message_game(int(number_1_30), secret_number)
                                                         )
                                         )
                response.set_cookie("number_1_30", str(number_1_30))
                if int(number_1_30) == secret_number:
                    response.set_cookie("secret_number", "")
                    return response
                return response






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