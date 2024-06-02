from flask import render_template, request, session, redirect, url_for
from classes.User import User

def register():
    return render_template("register.html", user="", password="", ulogin=session.get("user"), resul="")

def chkregister():
    user = request.form["user"]
    nome = request.form["nome"]
    email = request.form["email"]
    password = request.form["password"]
    ncartao = request.form["ncartao"]
    dvc = request.form["dvc"]
    cvc = request.form["cvc"]
    ntelemovel = request.form["ntelemovel"]
    saldo = request.form["saldo"]

    if user in User.obj:
        resul = "User already exists."
        return render_template("register.html", user=user, password=password, ulogin=session.get("user"), resul=resul)
    else:
        new_user = User(user, nome, email, password, ncartao, dvc, cvc, ntelemovel, saldo)
        User.obj[user] = new_user
        User.insert(user)
        User.lst.append(user)
        resul = "Registration successful."

        session["user"] = user
        return redirect(url_for('index'))
