from random import randint

from flask import Flask, render_template, request

from pymongo import MongoClient

client = MongoClient()
mydb = client.MEASI_STD_DB
mycol = mydb.std_details

webapp = Flask(__name__)


@webapp.route("/")
def home():
    if request.method == "POST":
        un_login = request.form["username"]
        pd_login = request.form["password"]

        result = mycol.find_one({"$and": [{"uname": un_login}, {"pwd": pd_login}]},
                                {"_id": 0, "uname": 0, "pwd": 0})  # projection 1 = show, 0 = dont show
        if result == None:
            return "invalid user"
        else:
            return render_template("booking_trial.html", result_html=result)  # jinja templating

        return render_template("booking.html")
    return render_template("home.html")


if __name__ == "__main__":
    webapp.run(debug=True)
