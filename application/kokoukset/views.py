from application import app, db
from flask import render_template, request
from application.kokoukset.models import Kokous

@app.route("/kokoukset/new/")
def tasks_form():
    return render_template("kokoukset/new.html")

@app.route("/kokoukset/", methods=["POST"])
def tasks_create():
    t = Kokous(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return "hello world!"
