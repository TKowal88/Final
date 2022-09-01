from flask import Flask, render_template, request, jsonify, session, redirect
from cs50 import SQL

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///warehouse.db")

app.secret_key = "secret key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        inventory = db.execute("SELECT * FROM stock ORDER BY code")
        print(inventory)
        storage = db.execute("SELECT * FROM storage WHERE rowid=1")
        print(storage)
        widthpercentage = []
        lengthpercentage = []
        for item in inventory:
            widthpercentage.append(round(item["boxwidth"] / (storage[0]["length"] / 100)))
            lengthpercentage.append(round(item["boxlength"] / (storage[0]["width"] / 100)))
        print(widthpercentage, lengthpercentage)
        # emptyspaces = int((100 // lengthpercentage) * (100 // widthpercentage) - len(inventory))        
        return render_template("index.html", inventory=inventory, lengthpercentage=lengthpercentage, widthpercentage=widthpercentage)
    else:
        code = request.form.get("code")
        name = request.form.get("name")
        boxwidth = request.form.get("boxwidth")
        boxlength = request.form.get("boxlength")
        boxheight = request.form.get("boxheight")
        db.execute("INSERT INTO stock (code, name, boxwidth, boxlength, boxheight) VALUES (?, ?, ?, ?, ?)", code, name, 
        boxwidth, boxlength, boxheight)
        return redirect("/")

@app.route("/storage", methods=["POST"])
def saveStorage():
    storageSize = request.get_json()
    print(storageSize)
    session["storageWidth"] = storageSize["width"]
    session["storageHeight"] = storageSize["height"]
    return "ok"

@app.route("/saved", methods=["POST"])
def coordinates():
    data = request.get_json()
    print(data)
    for row in data:
        left = round((row["left"] / session["storageWidth"]) * 100)
        top = round((row["top"] / session["storageHeight"]) * 100)
        db.execute("UPDATE stock SET x = ?, y = ? WHERE id = ?", left, top, row["id"])
    return "ok"

@app.route("/addStorage", methods=["POST"])
def addStorage():
    width = request.form.get("storageWidth")
    length = request.form.get("storageLength")
    height = request.form.get("storageHeight")
    db.execute("UPDATE storage SET width = ?, length = ?, height = ? WHERE rowid = 1", width, length, height)
    return redirect("/")

@app.route("/inventory")
def inventory():
    inventory = db.execute("SELECT * FROM stock ORDER BY code")
    return render_template("inventory.html", inventory=inventory)