from flask import Flask, render_template, request, session
from datafile import filename
from classes.User import User

app = Flask(__name__)

User.read(filename + 'business.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return render_template("login.html", user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = User.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    ulogin=session.get("user")
    if (ulogin != None):
        group = User.obj[ulogin].usergroup
        if group != "admin":
            User.current(ulogin)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = User.current()
            User.remove(obj.user)
            if not User.previous():
                User.first()
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            obj = User(request.form["user"],request.form["usergroup"], \
                            User.set_password(request.form["password"]))
            User.insert(obj.user)
            User.last()
        elif prev_option == 'edit' and option == 'save':
            obj = User.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = User.set_password(request.form["password"])
                print(obj.password)
            User.update(obj.user)
        elif option == "first":
            User.first()
        elif option == "previous":
            User.previous()
        elif option == "next":
            User.nextrec()
        elif option == "last":
            User.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = User.current()
        if option == 'insert' or len(User.lst) == 0:
            user = ""
            usergroup = ""
            password = ""
        else:
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, user=user,usergroup = usergroup,password=password, ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)

if __name__ == '__main__':
    app.run()