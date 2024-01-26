from flask import Flask, render_template, request, session, redirect, flash, send_from_directory, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from random import randint, choice
from werkzeug.utils import secure_filename
import json
import os
from util import generate_keysList

app = Flask(__name__)
app.secret_key = 'salmankhokhar'
# files upload configration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER = os.path.join("static", "uploads")
app_settings = json.load(open("settings.json", "r"))
# setting up database configration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
database = SQLAlchemy(app)
migrate = Migrate(app, database)
# list of domains allowed to access the API
allowed_websites = ["https://keey.es", "https://www.keey.es", "http://127.0.0.1:5500", "http://localhost:5500", "http://192.168.100.101:5500", "https://msalmankhokhar.github.io"]
cors = CORS(app, origins=allowed_websites)

class Platfroms(database.Model):
    name = database.Column(database.String(100), primary_key=True, nullable=False)
    valid_for = database.Column(database.String(100), unique=False, nullable=True)
class Softwares(database.Model):
    id = database.Column(database.String(50), primary_key=True, nullable=False)
    name = database.Column(database.String, nullable=True, unique=True)
    keys = database.Column(database.String, nullable=True, unique=False)
    versions = database.Column(database.String, nullable=True, unique=False)
    platforms = database.Column(database.String(100), nullable=True, unique=False)
    cracks = database.Column(database.String(500), nullable=True, unique=False)
    imgSrc = database.Column(database.String, nullable=True, unique=False)
    desc = database.Column(database.Text, nullable=True, unique=False)
class Games(database.Model):
    id = database.Column(database.String(50), primary_key=True, nullable=False)
    name = database.Column(database.String, nullable=True, unique=True)
    keys = database.Column(database.String, nullable=True, unique=False)
    versions = database.Column(database.String, nullable=True, unique=False)
    platforms = database.Column(database.String(100), nullable=True, unique=False)
    cracks = database.Column(database.String(500), nullable=True, unique=False)
    imgSrc = database.Column(database.String, nullable=True, unique=False)
    desc = database.Column(database.Text, nullable=True, unique=False)

# Command for database migrations and commit
# flask --app backend db migrate
# flask --app backend db upgrade

# creating database tables
with app.app_context():
    database.create_all()

@app.route("/api/getPlatforms/<string:type>/<string:id>", methods=["GET"])
def api_getPlatforms(type, id):
    sw = Softwares.query.filter_by(id=id).first()
    if type == "Game":
        sw = Games.query.filter_by(id=id).first()
    return json.loads(sw.platforms)

@app.route("/api/getKeys/<string:type>/<string:id>", methods=["GET"])
def api_getKeys(type, id):
    sw = Softwares.query.filter_by(id=id).first()
    if type == "Game":
        sw = Games.query.filter_by(id=id).first()
    return json.loads(sw.keys)

@app.route("/api/getVersions/<string:type>/<string:id>", methods=["GET"])
def api_getVersions(type, id):
    sw = Softwares.query.filter_by(id=id).first()
    if type == "Game":
        sw = Games.query.filter_by(id=id).first()
    return json.loads(sw.versions)

@app.route("/api/getCracks/<string:type>/<string:id>", methods=["GET"])
def api_getCracks(type, id):
    sw = Softwares.query.filter_by(id=id).first()
    if type == "Game":
        sw = Games.query.filter_by(id=id).first()
    return json.loads(sw.cracks)

def getPlatforms(software):
    return json.loads(software.platforms)
def getKeys(software):
    return json.loads(software.keys)
def getVersions(software):
    # print(f"software name is {software.name}")
    return json.loads(software.versions)
def getCracks(software):
    return json.loads(software.cracks)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/img/favicons'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(503)
def under_maintenance(e):
    return render_template('503.html'), 503

@app.route("/api/id_dict", methods=["GET"])
def api_totalData():
    # softwares = Softwares.query.all()
    softwares_id_dict = { sw.name : [sw.id, sw.imgSrc, "Software"] for sw in Softwares.query.all() }
    games_id_dict = { sw.name : [sw.id, sw.imgSrc, "Game"] for sw in Games.query.all() }
    return json.dumps(softwares_id_dict | games_id_dict)

@app.route("/api/getSoftwareInfo/<string:sw_id>", methods=["GET"])
def getSoftwareInfo(sw_id):
    software = Softwares.query.filter_by(id=sw_id).first()
    response = {
        "id" : software.id,
        "name" : software.name,
        "desc" : software.desc,
        "imgSrc" : software.imgSrc
    }
    return response

@app.route("/api/suggestions", methods=["GET"])
def api_sugg():
    # softwares = Softwares.query.all() + Games.query.all()
    sw_names = json.dumps([ sw.name for sw in Softwares.query.all()] + [ sw.name for sw in Games.query.all()])
    print(sw_names)
    return sw_names

@app.route("/product_key/<string:item>/<string:platfrom>/<string:id>", methods=["GET"])
def return_key(item, platfrom, id):
    sw = Softwares.query.filter_by(id=id).first()
    if item == "Game":
        sw = Games.query.filter_by(id=id).first()
    keysList = getKeys(sw)[platfrom]
    data_json = { "key" : choice(keysList) }
    return data_json

@app.route("/", methods=["GET"])
def home():
    softwares = Softwares.query.all()
    sw_names = json.dumps([ sw.name for sw in softwares])
    id_dict = json.dumps({ sw.name : [sw.id, sw.imgSrc] for sw in softwares })
    # print(sw_names)
    # print(id_dict)
    return render_template("home.html", sw_names= sw_names, id_dict=id_dict)

@app.route("/item/<string:type>/<string:id>", methods=["GET"])
def item(type, id):
    selected_software = Softwares.query.filter_by(id=id).first()
    if type == "Game":
        selected_software = Games.query.filter_by(id=id).first()
    if selected_software:
        return render_template("item.html", sw=selected_software, getPlatforms=getPlatforms, item=type)
    else:
        return "This software does not exist in our database"
    
@app.route("/choose/<string:item>/<string:platform>/<string:id>/<string:v>", methods=["GET"])
def choose(item, platform, id, v):
    selected_software = Softwares.query.filter_by(id=id).first()
    if v == "none":
        v = "Standard"
    if item == "Game":
        selected_software = Games.query.filter_by(id=id).first()
    if selected_software:
        keys = getKeys(selected_software)
        cracks = getCracks(selected_software)
        if platform in keys and platform in cracks:
            available_choices = "both"
        elif keys[platform]:
            available_choices = "Key"
        else:
            available_choices = "Crack"
        return render_template("choose.html", sw=selected_software, item=item, platform=platform, available=available_choices, v=v)
    else:
        return "This software does not exist in our database"
    
@app.route("/get_key/<string:item>/<string:platform>/<string:id>/<string:choice>/<string:v>", methods=["GET"])
def getKey(item, platform, id, choice, v):
    selected_software = Softwares.query.filter_by(id=id).first()
    if v == "none":
        v = "Standard"
    if item == "Game":
        selected_software = Games.query.filter_by(id=id).first()

    if selected_software:
        return render_template("getkey.html", sw=selected_software, item=item, platform=platform, choice=choice, v=v)
    else:
        return "This software does not exist in our database"

@app.route("/admin", methods=["GET"])
def admin():
    if request.method == "GET":
        if "adminuser" in session:
            return redirect("/admin/all/Software")
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

@app.route("/admin/all/<string:item>", methods=["GET"])
def admin_all_softwares(item):
    if request.method == "GET":
        if "adminuser" in session:
            currentNavlinkSpanText = "Softwares"
            if item == "Software":
                softwaresList = Softwares.query.all()
            elif item == "Game":
                softwaresList = Games.query.all()
                currentNavlinkSpanText = "Games"

            return render_template('admin/softwares.html', softwaresList=softwaresList, currentNavlinkSpanText=currentNavlinkSpanText, getPlatforms=getPlatforms, getKeys=getKeys, getCracks=getCracks, item=item, getVersions=getVersions)
        else:
            return redirect("/admin/login")

def generate_sw_ID():
    with app.app_context():
        while True:
            id = randint(1, 10000)
            print(f"generated sw id {id}")
            sw = Softwares.query.filter_by(id = id).first()
            if sw == None:
                return str(id)
            else:
                continue

@app.route("/download_crack/<string:item>/<string:sw_id>/<string:platform>", methods=["GET"])
def download_crack(item, sw_id, platform):
    if request.method == "GET":
        if item == "Software":
            software = Softwares.query.filter_by(id=sw_id).first()
        elif item == "Game":
            software = Games.query.filter_by(id=sw_id).first()
        cracksDict = json.loads(software.cracks)
        filename = cracksDict[platform]
        return send_file(os.path.join("static", "uploads", "Cracks", sw_id, platform, filename))

@app.route("/admin/add_new/<string:item>", methods=["GET", "POST"])
def admin_add_new_movie(item):
    print(f"item is get request is {item}")
    all_db_platforms = Platfroms.query.all()
    # platformValue_dict = {
    #     "platformWindows" : "Windows",
    #     "platformAndroid" : "Android",
    #     "platformMac" : "Mac",
    # }
    if request.method == "GET":
        if "adminuser" in session:
            return render_template('admin/add_new_software.html', item=item, all_db_platforms=all_db_platforms)
        else:
            return redirect("/admin/login")
    elif request.method == "POST":
        print(f"item is post request is {item}")
        id = generate_sw_ID()
        name = request.form.get('name')
        imgSrc = request.form.get('imgSrc')
        desc = request.form.get('desc')

        # PlatformList = [platformValue_dict[key] for key in platformValue_dict if request.form.get(key) == "on"]
        PlatformList = [pf.name for pf in all_db_platforms if request.form.get(f"platform{pf.name}") == "on"]
        keys = { key : generate_keysList(request.form.get(f"keyfor{key}")) for key in PlatformList if request.form.get(f"keyfor{key}") != "" }
        versions = { key : generate_keysList(request.form.get(f"vfor{key}")) for key in PlatformList if request.form.get(f"vfor{key}") != "" }
        cracks = [ pf.name for pf in all_db_platforms if request.form.get(f"crackfor{pf.name}") == "on" ]
        # print(keys)
        #uploading crack files:
        # for platform in PlatformList:
        #     file = request.files[f"filefor{platform}"]
        #     if file:
        #         save_directory = os.path.join(UPLOAD_FOLDER, "Cracks", id, platform)
        #         if not os.path.exists(save_directory):
        #             os.makedirs(save_directory, exist_ok=True)
        #         file_extention = os.path.splitext(file.filename)[1]
        #         allowed_extentions = [".zip", ".rar"]
        #         if file_extention in allowed_extentions:
        #             print(f"name is {name}")
        #             filename = secure_filename(f"{name.replace(' ', '_')}-{platform}" + file_extention)
        #             finalFilePath = os.path.join(save_directory, filename)
        #             file.save(finalFilePath)
        #             cracks[platform] = filename

        if item == "Software":            
            software = Softwares(
                id = id,
                name = name,
                imgSrc = imgSrc,
                # desc = desc,
                versions = json.dumps(versions),
                keys = json.dumps(keys),
                platforms = json.dumps(PlatformList),
                cracks = json.dumps(cracks)
            )
        elif item == "Game":
            software = Games(
                id = id,
                name = name,
                imgSrc = imgSrc,
                # desc = desc,
                versions = json.dumps(versions),
                keys = json.dumps(keys),
                platforms = json.dumps(PlatformList),
                cracks = json.dumps(cracks)
            )

        database.session.add(software)
        try:
            database.session.commit()
            flash(f"<strong>{name}</strong> added successfull in the database")
            print(f"{name} added successfull in the database")
        except Exception as e:
            flash(str(e))
        return redirect(f"/admin/all/{item}")

def getPlatformsText(software):
    return software.platforms
def getKeysText(software):
    return software.keys
def getVersionsText(software):
    return software.versions
def getCracksText(software):
    return software.cracks

@app.route("/admin/edit/<string:item>/<string:Id>", methods=["GET", "POST"])
def admin_edit_software(item, Id):
    if item == "Software":
        sw = Softwares.query.get(Id)
    elif item == "Game":
        sw = Games.query.get(Id)
    # platformValue_dict = {
    #     "platformWin" : "Windows",
    #     "platformAnd" : "Android",
    #     "platformMac" : "Mac",
    # }
    all_db_platforms = Platfroms.query.all()
    if request.method == "GET":
        if "adminuser" in session:
            if sw:
                return render_template('admin/edit_software.html', sw=sw, getCracksText=getCracksText, getKeysText=getKeysText, getPlatformsText=getPlatformsText, item=item, all_db_platforms=all_db_platforms, getVersionsText=getVersionsText)
            else:
                return "No software with this ID"
        else:
            return redirect("/admin/login")
    elif request.method == "POST":
        name = request.form.get('name')
        imgSrc = request.form.get('imgSrc')
        desc = request.form.get('desc')

        PlatformList = [pf.name for pf in all_db_platforms if request.form.get(f"platform{pf.name}") == "on"]
        keys = { key : generate_keysList(request.form.get(f"keyfor{key}")) for key in PlatformList if request.form.get(f"keyfor{key}") != "" }
        versions = { key : generate_keysList(request.form.get(f"vfor{key}")) for key in PlatformList if request.form.get(f"vfor{key}") != "" }
        cracks = [ pf.name for pf in all_db_platforms if request.form.get(f"crackfor{pf.name}") == "on" ]

        print(versions)
        # print(keys)
        #uploading crack files:
        # for platform in PlatformList:
        #     file = request.files[f"filefor{platform}"]
        #     if file:
        #         save_directory = os.path.join(UPLOAD_FOLDER, "Cracks", Id, platform)
        #         if not os.path.exists(save_directory):
        #             os.makedirs(save_directory, exist_ok=True)
        #         file_extention = os.path.splitext(file.filename)[1]
        #         allowed_extentions = [".zip", ".rar"]
        #         if file_extention in allowed_extentions:
        #             print(f"name is {name}")
        #             filename = secure_filename(f"{name.replace(' ', '_')}-{platform}" + file_extention)
        #             finalFilePath = os.path.join(save_directory, filename)
        #             file.save(finalFilePath)
        #             cracks[platform] = filename

        sw.name = name
        sw.imgSrc = imgSrc
        # sw.desc = desc
        sw.keys = json.dumps(keys)
        sw.platforms = json.dumps(PlatformList)
        sw.versions = json.dumps(versions)
        if len(cracks) > 0:
            sw.cracks = json.dumps(cracks)

        try:
            database.session.commit()
            flash(f"<strong>{name}</strong> updated successfully in the database")
            print(f"{name} updated successfully in the database")
        except Exception as e:
            flash(str(e))
        return redirect(f"/admin/all/{item}")
    
@app.route("/admin/delete/<string:item>/<string:Id>", methods=["GET"])
def admin_delete_software(item, Id):
    if request.method == "GET":
        if "adminuser" in session:
            if item == "Software":
                selected_sw = Softwares.query.filter_by(id=Id).first()
            elif item == "Game":
                selected_sw = Games.query.filter_by(id=Id).first()
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