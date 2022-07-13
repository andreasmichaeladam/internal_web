from flask import Blueprint, render_template,session,request,url_for,redirect,flash
from datetime import datetime , timedelta   
from internal_web import *

admin_page = Blueprint("admin_page", __name__, static_folder="static", template_folder="templates" )

@admin_page.errorhandler(404)
def not_found(e):
 return render_template("404.html"),404

#Login area
@admin_page.route("/login", methods=["POST","GET"])
def login():
    if "admin" in session:
        return redirect(url_for('.admin'))
    else : 
        if request.method =="POST":
            name = request.form["nm"]
            pasf = request.form["ps"]
            users = user.query.filter_by(name = name ).first()
            if users and users.role and pasf == users._pass:
                session ["admin"] = name
                print("login as admin")
                return redirect(url_for('.admin'))
            elif users and not users.role and pasf == users._pass :
                session ["guess"] = name
                print("login as guess")
                return redirect(url_for('.admin'))
            flash("Please check your email and password correctly")
            return render_template("login.html")
        return render_template("login.html")


@admin_page.route("/logout")
def logout():
    if "admin" in session or "guess" in session :
        session.pop("admin",None) or session.pop("guess",None)
        return redirect(url_for('home'))
    return redirect(url_for('home'))

#admin site
@admin_page.route("/", methods=["GET","POST"])
def admin():
    if "admin" in session:
        #from database import contacts
        return redirect(url_for('.blog'))
    elif "guess" in session:
        # from database import contacts,user
        return render_template("index.html")
    return redirect(url_for('home'))

@admin_page.route("/userdata", methods=["GET", "POST"])
def blog():
    if "admin" in session:
        from internal_web import userdat
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        sesi=datetime.now()
        twodays= timedelta(minutes=5)
        userdat = userdat.query.all()
        return render_template("blog_table.html", userdat=userdat,sesi = sesi,twodays=twodays)
    elif "guess" in session:
        from internal_web import userdat
        userdat = userdat.query.all()
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        return render_template("blog_table_guess.html", userdat=userdat)
    return redirect(url_for('home'))

@admin_page.route("/userdata/twodays",methods=["GET", "POST"])
def two():
    if "admin" in session:
        from internal_web import userdat
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        sesi=datetime.now()
        twodays= timedelta(minutes=5)
        userdat = userdat.query.all()
        return render_template("blog_twodays.html", userdat=userdat,sesi = sesi,twodays=twodays)
    elif "guess" in session:
        from internal_web import userdat
        userdat = userdat.query.all()
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        return render_template("blog_table_guess.html", userdat=userdat)
    return redirect(url_for('home'))    

@admin_page.route("/userdata/relog/<username>",methods=["GET", "POST"])
def relog(username):
    if "admin" in session:
        from internal_web import userdat
        userdat = userdat.query.filter_by(name = username).first()
        if not userdat:
            return render_template("404.html"),404
        else:
            gettime = datetime.now()
            userdat._date = gettime
            db.session.commit()
            return redirect(url_for('.two')) 
    elif "guess" in session:
        from internal_web import userdat
        userdat = userdat.query.all()
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        return render_template("blog_table_guess.html", userdat=userdat)
    return redirect(url_for('home'))    

@admin_page.route("/userdata/search/<id>",methods=["GET","POST"])
def sblog(id):
    if "admin" in session :
        from internal_web import userdat
        userdat = userdat.query.filter(userdat.name.like(id)).all()
        sesi=datetime.now()
        twodays= timedelta(minutes=5)
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        return render_template("blog_table.html", userdat=userdat,sesi = sesi,twodays=twodays)
    elif "guess" in session:
        from internal_web import userdat
        userdat = userdat.query.filter(userdat.name.like(id)).all()
        if request.method =="POST" :
            table_search = request.form["table_search"].rstrip()
            search = "%{}%".format(table_search)
            return redirect(url_for('.sblog',id=search))
        return render_template("blog_table_guess.html", userdat=userdat)
    return redirect(url_for('home'))

@admin_page.route("/userdata/edit/<blog_e>", methods = ["POST","GET"])
def edit_blog(blog_e):
    if "admin" in session :
        from internal_web import userdat
        userdat = userdat.query.filter_by(name = blog_e ).first()
        if not blog :
            return render_template("404.html"),404
        else : 
            if request.method =="POST":
                    s = request.form["name"]
                    name = s.rstrip(" ")
                    z = request.form["telp"]
                    telp = z.rstrip(" ")
                    userdat.name = name
                    userdat.telp = telp
                    db.session.commit()
                    return redirect(url_for('admin_page.blog'))
            return render_template("edit_blog.html", userdat = userdat)
    return redirect(url_for('home'))

@admin_page.route("/userdata/delete/<blog_>", methods = ["POST","GET"])
def delete_blog(blog_):
    if "admin" in session :
        from internal_web import userdat
        userdat = userdat.query.filter_by(name = blog_ ).first()
        if not blog :
            return render_template("404.html"),404
        db.session.delete(userdat)
        db.session.commit()
        return redirect(url_for('admin_page.blog'))
    return redirect(url_for('home'))

@admin_page.route("/userdata/add", methods = ["POST","GET"])
def add_blog():
    if "admin" in session :
        from internal_web import userdat
        if request.method =="POST":
                    s = request.form["name"]
                    name = s.strip()
                    z = request.form["telp"]
                    telp = z.rstrip(" ")
                    date = datetime.now()
                    userdat = userdat(name,telp,date)
                    db.session.add(userdat)
                    db.session.commit()
                    return redirect(url_for('admin_page.blog')) 
        return render_template("add_blog.html")
    return redirect(url_for('home'))
