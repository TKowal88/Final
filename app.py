from flask import Flask, render_template, request
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///warehouse.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        inventory = db.execute("SELECT * FROM stock ORDER BY code")
        boxlength = 50
        storagewidth = 235
        boxwidth = 35
        storagelength = 590
        widthpercentage = boxwidth / (storagelength / 100)
        lengthpercentage = boxlength / (storagewidth / 100)
        emptyspaces = int((100 // lengthpercentage) * (100 // widthpercentage) - len(inventory))
        
        return render_template("index.html", inventory=inventory, len = emptyspaces, lengthpercentage=lengthpercentage, widthpercentage=widthpercentage)
    else:
        code = request.form.get("code")
        name = request.form.get("name")
        db.execute("INSERT INTO stock (code, name) VALUES (?, ?)", code, name)
        inventory = db.execute("SELECT * FROM stock ORDER BY code")
        boxlength = 50
        storagewidth = 235
        storagelength = 590
        boxwidth = 35
        widthpercentage = boxwidth // (storagelength / 100)
        lengthpercentage = boxlength // (storagewidth / 100)
        return render_template("index.html", inventory=inventory, lengthpercentage=lengthpercentage, widthpercentage=widthpercentage)

@app.route("/inventory")
def inventory():
    inventory = db.execute("SELECT * FROM stock ORDER BY code")
    return render_template("inventory.html", inventory=inventory)