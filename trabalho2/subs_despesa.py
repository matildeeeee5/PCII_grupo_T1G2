from flask import Flask, render_template, request, session
from classes.Despesas import Despesas
from classes.Grupo import Grupo
from classes.User import User
from classes.Viagem import Viagem

prev_option = ""

def gform(cname='', submenu=""):
    global prev_option
    ulogin = session.get("user")
    grupo_not_found = False
    if ulogin is not None:
        cl = eval(cname)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            if cl.auto_number == 1:
                strobj = "None"
            else:
                strobj = request.form[cl.att[0]]
            for i in range(1, len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            idgrupo = request.form['_idgrupo']
            if idgrupo in Grupo.obj:
                obj = cl.from_string(strobj)
                cl.insert(getattr(obj, cl.att[0]))
                cl.last()
            else:
                grupo_not_found = True
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(cl.auto_number, len(cl.att)):
                att = cl.att[i]
                setattr(obj, att, request.form[att])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                cl.remove(obj.idcompra)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        if obj:
            obj_dict = obj.__dict__
            if hasattr(obj, '_valorpp'):
                obj_dict['_valorpp'] = obj._valorpp
        else:
            obj_dict = {att: "" for att in cl.att}

        if cname == 'Despesas':
            return render_template("despesas.html", butshow=butshow, butedit=butedit,
                                   cname=cname, obj=obj_dict, att=cl.att, header=cl.header, des=cl.des,
                                   ulogin=session.get("user"), auto_number=cl.auto_number,
                                   submenu=submenu, grupo_not_found=grupo_not_found)
        else:
            return render_template("gform.html", butshow=butshow, butedit=butedit,
                                   cname=cname, obj=obj_dict, att=cl.att, header=cl.header, des=cl.des,
                                   ulogin=session.get("user"), auto_number=cl.auto_number,
                                   submenu=submenu, grupo_not_found=grupo_not_found)
    else:
        return render_template("index.html", ulogin=ulogin)


