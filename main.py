from flask import Flask, render_template, request, make_response
import datetime
import random

app = Flask(__name__)
number = random.randint(1, 40)


@app.route("/")
def index():
    some_number = request.cookies.get("some_number")
    user_name = request.cookies.get("user_name")
    if user_name:
        some_text = user_name + ",  mesta iz vrha tvoje glave so: "
    else:
        some_text = "Mesta iz vrha glave so: "
    current_year = datetime.datetime.now().year
    current_hour = datetime.datetime.now().minute
    cities = ["Boston", "Vienna", "Paris", "Berlin"]
    currency = ["$", "€", "tolar", "dinar", "kuna", "lira"]
    calc = number * 21

    return render_template("index.html", number=some_number, currency=currency, calc=calc, some_text=some_text, current_year=current_year, current_hour=current_hour, cities=cities, name=user_name)


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
        message = "Congratulations, you guessed the number!"
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
        if not secret_number:
            secret_number = random.randint(1, 30)
            number_1_30 = request.form.get("number_1_30")
            response = make_response(render_template("guess.html", number_1_30=number_1_30))
            response.set_cookie("number_1_30", number_1_30)
            response.set_cookie("secret_number", str(secret_number))
            return response
        else:
            number_1_30 = int(request.form.get("number_1_30"))
            secret_number = int(secret_number)
            response = make_response(render_template("guess.html",
                                                     number_1_30=number_1_30,
                                                     message=message_game(number_1_30, secret_number)
                                                     )
                                     )
            response.set_cookie("number_1_30", str(number_1_30))
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