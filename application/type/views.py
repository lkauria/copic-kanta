from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.type.models import Type
from application.type.forms import TypeForm

@app.route("/type/new/")
@login_required
def type_form():
        return render_template("type/new.html", form = TypeForm())

@app.route("/type/", methods=["POST"])
@login_required
def type_create():
    form = TypeForm(request.form)

    if not form.validate():
       return render_template("type/new.html", form = form)

    type = Type(form.name.data)

    db.session().add(type)
    db.session().commit()

    return redirect(url_for("items_index"))

