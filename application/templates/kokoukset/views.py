from application import app, db
from flask import render_template, request
from application.kokoukset.models import Kokous

@app.route("/kokoukset", methods=["GET"])
def tasks_index():
    return render_template("kokoukset/list.html", kokoukset = Kokous.query.all())

@app.route("/kokoukset/new/")
def tasks_form():
    return render_template("kokoukset/new.html")

@app.route("/kokoukset/", methods=["POST"])
def tasks_create():
    t = Kokous(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("kokoukset_index"))

