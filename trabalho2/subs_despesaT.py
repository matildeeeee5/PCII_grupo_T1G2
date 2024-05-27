from flask import Flask, render_template, request, session

from classes.Despesas import Despesas
from classes.Grupo import Grupo
from classes.User import User
from classes.Viagem import Viagem

prev_option = ""

def gformT(cname='', submenu=""):
    global prev_option
    
    ulogin = session.get("user")
    if ulogin is not None:
        sbl = eval(cname)
        option = request.args.get("option")
        
        if option == 'exit':
            return render_template("index.html", ulogin=session.get("user")) 

        prev_option = option

        headers = list()
        for i in range(1, len(sbl.att)): 
                headers.append(sbl.att[i][1:])        
        objl = list()
        for line in sbl.lst:
            objl.append(sbl.obj[line])

        return render_template("despesasT.html", butshow="disabled", butedit="disabled",
                    cname=cname, 
                    ulogin=session.get("user"), objl=objl, headerl=sbl.header,
                    desl=sbl.des, attl=sbl.att,
                    submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)
