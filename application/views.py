from application import app, db
from flask import redirect, render_template, request, url_for
from application.kokoukset.models import Kokous

@app.route("/kokoukset", methods=["GET"])
def kokoukset_index():
    return render_template("kokoukset/list.html", kokoukset = Kokous.query.all())

@app.route("/kokoukset/new/")
def kokoukset_form():
    return render_template("kokoukset/new.html")

@app.route("/kokoukset/<kokous_id>/", methods=["POST"])
def kokoukset_set_done(kokous_id):

    t = Kokous.query.get(kokous_id)
    t.done = True
    db.session().commit()

    return redirect(url_for("kokoukset_index"))

@app.route("/kokoukset/", methods=["POST"])
def kokoukset_create():
    t = Kokous(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("kokoukset_index"))
