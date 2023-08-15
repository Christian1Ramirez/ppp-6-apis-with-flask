import json
from flask import Blueprint, render_template, request, redirect
from .models import Reptile, db

reptile_bp = Blueprint("reptile_bp", __name__, url_prefix="/reptiles")

@reptile_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        submitter = request.form["submitter"]
        reptile_id = int(request.form["reptile_id"])
        reptile_name = request.form["reptile_name"]
        reptile_fact = request.form["reptile_fact"]

        new_reptile = Reptile(reptile_id=reptile_id, reptile_name=reptile_name, reptile_fact=reptile_fact)
        db.session.add(new_reptile)
        db.session.commit()

        return redirect("/reptiles")

    reptiles = json.load(open("reptiles.json"))
    return render_template("index.html", reptiles=reptiles)

@reptile_bp.route("/<int:id>")
def show(id):
    reptile = Reptile.query.filter_by(reptile_id=id).first()
    if reptile:
        return f"Reptile Details: ID {reptile.reptile_id}, Name {reptile.reptile_name}, Fact {reptile.reptile_fact}"
    else:
        return "Reptile not found"
