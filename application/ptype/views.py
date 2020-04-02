from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.ptype.models import Ptype
from application.ptype.forms import PtypeForm

@app.route("/ptype/new/")
@login_required
def ptype_form():
        return render_template("ptype/new.html", form = PtypeForm())

@app.route("/ptype/", methods=["POST"])
@login_required
def ptype_create():
    form = PtypeForm(request.form)

    if not form.validate():
       return render_template("ptype/new.html", form = form)

    ptype = Ptype(form.name.data)

    db.session().add(ptype)
    db.session().commit()

    return redirect(url_for("items_index"))

