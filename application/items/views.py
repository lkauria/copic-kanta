from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm

@app.route("/items/", methods=["GET"])
def items_index():
	return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
@login_required
def items_form():
	return render_template("items/new.html", form = ItemForm())

@app.route("/items/<item_id>/", methods=["POST"])
@login_required
def items_set_lowink(item_id):

    item = Item.query.get(item_id)
    item.lowink = True
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
       return render_template("items/new.html", form = form)

    item = Item(form.name.data, form.type.data)
    item.lowink = form.lowink.data
    item.account_id = current_user.id

    db.session().add(item)
    db.session().commit()

    return redirect(url_for("items_index"))
