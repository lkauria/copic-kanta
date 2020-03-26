from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm

@app.route("/items/", methods=["GET"])
def items_index():
	return render_template("items/list.html", items = Item.query.all())


@app.route("/items/myitems/", methods=["GET"])
@login_required
def items_myindex():
        return render_template("items/list.html", items =
               Item.query.filter(Item.account_id == current_user.id))


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

@app.route("/items/delete/<item_id>/", methods=["POST"])
@login_required
def items_delete(item_id):

    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session().commit()

    return redirect(url_for("items_index"))



@app.route("/items/", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
       return render_template("items/new.html", form = form)

    item = Item(form.name.data, form.colorcode.data, form.type.data)
    item.lowink = form.lowink.data
    item.account_id = current_user.id
    item.colorcode = form.colorcode.data

    db.session().add(item)
    db.session().commit()

    return redirect(url_for("items_index"))
