from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task

@app.route("/kokoukset", methods=["GET"])
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all())

@app.route("/kokoukset/new/")
def tasks_form():
    return render_template("tasks/new.html")

@app.route("/kokoukset/", methods=["POST"])
def tasks_create():
    t = Task(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))
