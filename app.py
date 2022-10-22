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
        storages = db.execute("SELECT * FROM storage")
        if session["storageName"] == "":
            session["storageName"] = storages[0]["name"]

        
        else:
            storage = db.execute("SELECT * FROM storage WHERE name = ?", session["storageName"])
        stock = db.execute("SELECT * FROM stock ")
        
        widthpercentage = []
        lengthpercentage = []
        for item in stacks:
            widthpercentage.append(round(item["stackwidth"] / (storage[0]["length"] / 100)))
            lengthpercentage.append(round(item["stacklength"] / (storage[0]["width"] / 100)))
        # emptyspaces = int((100 // lengthpercentage) * (100 // widthpercentage) - len(inventory))        
        return render_template("index.html", stacks=stacks, stock=stock, lengthpercentage=lengthpercentage, widthpercentage=widthpercentage, storages=storages, storage=storage)
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

@app.route("/selectstorage", methods=["POST"])
def selectStorage():
    session["storageName"] = request.form.get("storagename")
    return redirect("/")

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
    name = request.form.get("storageName")
    width = request.form.get("storageWidth")
    length = request.form.get("storageLength")
    height = request.form.get("storageHeight")
    db.execute("INSERT INTO storage VALUES (?, ?, ?, ?)", name, width, length, height)
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
    boxcount = int(request.form.get("boxcount"))
    for i in range(0, boxcount):
        db.execute("INSERT INTO stock (code, name, boxlength, boxwidth, boxheight) VALUES (?, ?, ?, ?, ?)", code, name, boxlength, boxwidth, boxheight)
    return redirect("/")


@app.route("/stock")
def inventory():
    inventory = db.execute("SELECT * FROM stock ORDER BY stock_id")
    stacks = db.execute("SELECT * FROM stacks ORDER BY id")
    return render_template("inventory.html", inventory=inventory, stacks=stacks)

@app.route("/updatestacks", methods=["POST"])
def updatestacks():
    stock = db.execute("SELECT * FROM stock ORDER BY stock_id")
    update = []
    for item in stock:
        pair = {}
        pair[item["stock_id"]] = (request.form.get(str(item["stock_id"])))
        print(pair)
        if pair[item["stock_id"]] != '':
            db.execute("UPDATE stock SET stack_id = ? WHERE stock_id = ?", pair[item["stock_id"]], item["stock_id"])
    

    return redirect("/stock")