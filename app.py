from flask import Flask, render_template, request, jsonify, session, redirect
from cs50 import SQL

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///warehouse.db")

app.secret_key = "secret key"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        stacks = db.execute("SELECT * FROM stacks ORDER BY id")
        storage = db.execute("SELECT * FROM storage WHERE rowid=1")
        widthpercentage = []
        lengthpercentage = []
        for item in stacks:
            widthpercentage.append(round(item["stackwidth"] / (storage[0]["length"] / 100)))
            lengthpercentage.append(round(item["stacklength"] / (storage[0]["width"] / 100)))
        # emptyspaces = int((100 // lengthpercentage) * (100 // widthpercentage) - len(inventory))        
        return render_template("index.html", stacks=stacks, lengthpercentage=lengthpercentage, widthpercentage=widthpercentage, storage=storage)
    else:
        
        stackwidth = request.form.get("stackwidth")
        stacklength = request.form.get("stacklength")
        storage = db.execute("SELECT * FROM storage WHERE rowid=1")
        stackheight = storage[0]["height"]
        db.execute("INSERT INTO stacks (stackwidth, stacklength, stackheight) VALUES (?, ?, ?)" , stackwidth, stacklength, stackheight)
        return redirect("/")

@app.route("/storage", methods=["POST"])
def saveStorage():
    storageSize = request.get_json()
    session["storageWidth"] = storageSize["width"]
    session["storageHeight"] = storageSize["height"]
    return "ok"

@app.route("/saved", methods=["POST"])
def coordinates():
    data = request.get_json() 
    for row in data:
        left = round((row["left"] / session["storageWidth"]) * 100)
        top = round((row["top"] / session["storageHeight"]) * 100)
        db.execute("UPDATE stacks SET x = ?, y = ? WHERE id = ?", left, top, row["id"])
    return "ok"

@app.route("/addStorage", methods=["POST"])
def addStorage():
    width = request.form.get("storageWidth")
    length = request.form.get("storageLength")
    height = request.form.get("storageHeight")
    db.execute("UPDATE storage SET width = ?, length = ?, height = ? WHERE rowid = 1", width, length, height)
    return redirect("/")

@app.route("/removestack", methods=["POST"])
def removeItem():
    id = request.form.get("id")
    db.execute("DELETE FROM stacks WHERE id = ?", id)
    return redirect("/")

@app.route("/rotatestack", methods=["POST"])
def rotateItem():
    id = request.form.get("id")
    newstackwidth = db.execute("SELECT stacklength FROM stacks WHERE id = ?", id)
    newstacklength = db.execute("SELECT stackwidth FROM stacks WHERE id = ?", id)
    db.execute("UPDATE stacks SET stackwidth = ?, stacklength = ? WHERE id = ?", newstackwidth[0]["stacklength"], newstacklength[0]["stackwidth"], id)
    return redirect("/")

@app.route("/addstock", methods=["POST"])
def addStock():
    code = request.form.get("code")
    name = request.form.get("name")
    boxwidth = request.form.get("boxwidth")
    boxlength = request.form.get("boxlength")
    boxheight = request.form.get("boxheight")
    boxcount = request.form.get("boxcount")
    db.execute("INSERT INTO stock (code, name, boxlength, boxwidth, boxheight) VALUES (?, ?, ?, ?, ?)", code, name, boxlength, boxwidth, boxheight)
    return redirect("/")


@app.route("/stock")
def inventory():
    inventory = db.execute("SELECT * FROM stock ORDER BY stock_id")
    return render_template("inventory.html", inventory=inventory)