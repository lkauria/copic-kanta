from application import app, db
from flask import render_template, request, redirect, url_for
from application.items.models import Item

@app.route("/items/", methods=["GET"])
def items_index():
	return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
	return render_template("items/new.html")

@app.route("/items/<item_id>/", methods=["POST"])
def items_set_lowink(item_id):

    item = Item.query.get(item_id)
    item.lowink = True
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
def items_create():
    item = Item(request.form.get("name"))

    db.session().add(item)
    db.session().commit()

    return redirect(url_for("items_index"))
