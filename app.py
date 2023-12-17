from flask import Flask, render_template, request, session, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from random import randint, choices
import json
import os

app = Flask(__name__)
app.secret_key = 'salmankhokhar'

# files upload configration
# UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER = 'static/uploads'

app_settings = json.load(open("settings.json", "r"))

# setting up database configration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
database = SQLAlchemy(app)
migrate = Migrate(app, database)

class Softwares(database.Model):
    id = database.Column(database.String(50), primary_key=True, nullable=False)
    name = database.Column(database.String, nullable=False, unique=True)
    key = database.Column(database.String(100), nullable=True, unique=False)
    imgSrc = database.Column(database.String, nullable=True, unique=False)
    tags = database.Column(database.String, nullable=True, unique=False)
    desc = database.Column(database.Text, nullable=True, unique=False)

# Command for database migrations and commit
# flask --app backend db migrate
# flask --app backend db upgrade

# creating database tables
with app.app_context():
    database.create_all()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/favicons'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(503)
def under_maintenance(e):
    return render_template('503.html'), 503

@app.route("/api/total_data", methods=["GET"])
def api_totalData():
    Software_List = Softwares.query.all()
    data_json = [ 
        { 
            software.name : { "id" : software.id, "image-link" : software.imgSrc, "description" : software.desc, "product-key" : software.key }
        } 
        for software in Software_List 
        ]
    return data_json

@app.route("/api/suggestions", methods=["GET"])
def api_sugg():
    Software_List = Softwares.query.all()
    data_json = [ sw.name for sw in Software_List]
    return data_json

@app.route("/product_key/<string:id>", methods=["GET"])
def return_key(id):
    sw = Softwares.query.filter_by(id=id).first()
    data_json = { "key" : sw.key }
    return data_json

@app.route("/", methods=["GET"])
def home():
    softwares = Softwares.query.all()
    sw_names = json.dumps([ sw.name for sw in softwares])
    id_dict = json.dumps({ sw.name : [sw.id, sw.imgSrc] for sw in softwares })
    print(sw_names)
    print(id_dict)
    return render_template("home.html", sw_names= sw_names, id_dict=id_dict)

@app.route("/item/<string:id>", methods=["GET"])
def item(id):
    selected_software = Softwares.query.filter_by(id=id).first()
    if selected_software:
        return render_template("item.html", sw=selected_software)
    else:
        return "This software does not exist in our database"
    
@app.route("/get_key/<string:id>", methods=["GET"])
def getKey(id):
    selected_software = Softwares.query.filter_by(id=id).first()
    if selected_software:
        return render_template("getkey.html", sw=selected_software)
    else:
        return "This software does not exist in our database"

@app.route("/admin", methods=["GET"])
def admin():
    if request.method == "GET":
        if "adminuser" in session:
            return redirect("/admin/all_softwares")
        else:
            return redirect("/admin/login")
        
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        if "adminuser" not in session:
            return render_template("/admin/login.html")
        else:
            return redirect("/admin")
    elif request.method == "POST":
        password = request.form.get("password")
        if password == app_settings["adminPassword"]:
            session["adminuser"] = True
            return redirect("/admin")
        else:
            return "<h1 style='margin: 15px;'>Wrong password try Again</h1>"
        
@app.route("/admin/all_softwares", methods=["GET"])
def admin_all_softwares():
    if request.method == "GET":
        if "adminuser" in session:
            softwaresList = Softwares.query.all()
            return render_template('admin/softwares.html', softwaresList=softwaresList, currentNavlinkSpanText="Softwares")
        else:
            return redirect("/admin/login")

def generate_sw_ID():
    with app.app_context():
        while True:
            id = randint(100000, 999999)
            print(f"generated sw id {id}")
            sw = Softwares.query.filter_by(id = id).first()
            if sw == None:
                return id
            else:
                continue

@app.route("/admin/add_new_software", methods=["GET", "POST"])
def admin_add_new_movie():
    if request.method == "GET":
        if "adminuser" in session:
            return render_template('admin/add_new_software.html')
        else:
            return redirect("/admin/login")
    elif request.method == "POST":
        id = generate_sw_ID()
        name = request.form.get('name')
        key = request.form.get('key')
        imgSrc = request.form.get('imgSrc')
        tags = request.form.get('tags')
        desc = request.form.get('desc')

        sw = Softwares(
            id = id,
            name = name,
            key = key,
            tags = tags,
            imgSrc = imgSrc,
            desc = desc
        )

        database.session.add(sw)
        try:
            database.session.commit()
            flash(f"{name} added successfull in the database")
            print(f"{name} added successfull in the database")
        except Exception as e:
            flash(str(e))
        return redirect("/admin")
    
@app.route("/admin/edit_software/<string:Id>", methods=["GET", "POST"])
def admin_edit_software(Id):
    sw = Softwares.query.get(Id)
    if request.method == "GET":
        if "adminuser" in session:
            if sw:
                return render_template('admin/edit_software.html', sw=sw)
            else:
                return "No software with this ID"
        else:
            return redirect("/admin/login")
    elif request.method == "POST":
        name = request.form.get('name')
        key = request.form.get('key')
        imgSrc = request.form.get('imgSrc')
        tags = request.form.get('tags')
        desc = request.form.get('desc')

        sw.name = name
        sw.key = key
        sw.tags = tags
        sw.imgSrc = imgSrc
        sw.desc = desc

        try:
            database.session.commit()
            flash(f"{name} updated successfully in the database")
            print(f"{name} updated successfully in the database")
        except Exception as e:
            flash(str(e))
        return redirect("/admin")
    
@app.route("/admin/delete_software/<string:Id>", methods=["GET"])
def admin_delete_software(Id):
    if request.method == "GET":
        if "adminuser" in session:
            selected_sw = Softwares.query.filter_by(id=Id).first()
            database.session.delete(selected_sw)
            database.session.commit()
            return redirect('/admin')
        else:
            return redirect("/admin/login")
        
@app.route("/admin/logout", methods=["GET"])
def admin_logout():
    if request.method == "GET":
        if "adminuser" in session:
            session.pop("adminuser")
            return redirect("/admin/login")
        else:
            return redirect("/admin/login")
        
