# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: subs_gformT.py

"""""
from flask import Flask, render_template, request, session

from classes.Despesas import Despesas
from classes.Grupo import Grupo
from classes.User import User
from classes.Viagem import Viagem

prev_option = ""

def gformT(cname='',submenu=""):
    global prev_option
    
    #scname = eval(cname)
    ulogin=session.get("user")
    if (ulogin != None):
        print(cname)
        sbl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            print("prev_option == 'insert' and option == 'save':")
        elif prev_option == 'edit' and option == 'save':
            print("prev_option == 'edit' and option == 'save':")
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                print('option == "delete":')
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                #cl.first()
                print('option == "first":')
            elif option == "previous":
                #cl.previous()
                print('option == "previous":')
            elif option == "next":
                #cl.nextrec()
                print('option == "next":')
            elif option == "last":
                #cl.last()
                print('option == "last":')
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
               
                sbl.remove(sbl.lst[row])
                if not sbl.previous():
                    sbl.first()
                
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
               
                if (sbl.auto_number == 1):
                    strobj = "None"
                else:
                    strobj = request.form[sbl.att[0]]
                for i in range(1,len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                print (strobj)
                objl = sbl.from_string(strobj)
                #code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                code = str(getattr(objl, sbl.att[0]))
                sbl.insert(code)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user")) 
        
        headers = list()
        
        for i in range(1, len(sbl.att)): 
                headers.append(sbl.att[i][1:])        
        objl = list()
        for line in sbl.lst:
            objl.append(sbl.obj[line])
        return render_template("gformT.html", butshow=butshow, butedit=butedit,
                    cname=cname, 
                    ulogin=session.get("user"),objl=objl,headerl=sbl.header,
                    desl=sbl.des, attl=sbl.att,
                    submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)

