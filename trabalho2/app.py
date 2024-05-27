from flask import Flask, render_template, request, session
from datafile import filename

import os

from classes.Despesas import Despesas
from classes.Grupo import Grupo
from classes.User import User
from classes.Viagem import Viagem

app = Flask(__name__)

User.read(filename + 'user.db')
Viagem.read(filename + 'user.db')
Grupo.read(filename + 'user.db')
Despesas.read(filename + 'user.db')

prev_option = ""
submenu = ""
app.secret_key = 'BAD_SECRET_KEY'

upload_folder = os.path.join('static', 'images')
app.config['UPLOAD'] = upload_folder


import subs_login as lsub
import subs_gform as gfsub
import subs_gformT as gfTsub
import subs_despesa as despesasub
import subs_despesaT as despesaTsub
import subs_grupo as subgrupo
import subs_grupoT as grupoTsub

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return lsub.login()

@app.route("/logoff")
def logoff():
    return lsub.logoff()

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    return lsub.chklogin()

@app.route("/submenu", methods=["post","get"])
def getsubm():
    global submenu
    submenu = request.args.get("subm")
    return render_template("index.html", ulogin=session.get("user"),submenu=submenu)

@app.route("/gform/<cname>", methods=["post","get"])
def gform(cname=''):
    submenu = request.args.get("subm")
    return gfsub.gform(cname,submenu)


@app.route("/gformT/<cname>", methods=["post","get"])
def gformT(cname=''):
    submenu = request.args.get("subm")
    return gfTsub.gformT(cname,submenu)

@app.route("/despesaT/<cname>", methods=["post", "get"])
def despesaT(cname=''):
    submenu = request.args.get("subm")
    return despesaTsub.gformT(cname, submenu)

@app.route("/grupoT/<cname>", methods=["post", "get"])
def grupoT(cname=''):
    submenu = request.args.get("subm")
    return grupoTsub.gformT(cname, submenu)


@app.route("/despesa/<cname>", methods=["post","get"])
def despesa(cname=''):
    submenu = request.args.get("subm")
    return despesasub.gform(cname, submenu)

@app.route("/grupo/<cname>", methods=["post","get"])
def grupo(cname=''):
    submenu = request.args.get("subm")
    return subgrupo.gform(cname, submenu)

   
if __name__ == '__main__':
    app.run(debug=True)
    #app.run()
    