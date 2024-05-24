
from flask import Flask, render_template, request, session

from classes.Despesas import Despesas
from classes.Grupo import Grupo
from classes.User import User
from classes.Viagem import Viagem

prev_option = ""

def despesasform(cname='', submenu=""):
    global prev_option
    ulogin = session.get("user")
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
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            # if auto_number = 1 the key stays the same
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
                cl.remove(obj.code)
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
            if hasattr(obj, '_valorpp'):  # Check if the attribute exists
                obj_dict['_valorpp'] = obj._valorpp  # Add _valorpp to the dictionary
        else:
            obj_dict = {att: "" for att in cl.att}
        return render_template("gform.html", butshow=butshow, butedit=butedit,
                               cname=cname, obj=obj_dict, att=cl.att, header=cl.header, des=cl.des,
                               ulogin=session.get("user"), auto_number=cl.auto_number,
                               submenu=submenu)
    else:
        return render_template("index.html", ulogin=ulogin)

