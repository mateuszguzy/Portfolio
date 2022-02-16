import os
from dotenv import load_dotenv
from functools import wraps
from forms import FiltersForm, RegisterUser, LoginUser, AddCafe
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import exc
from flask import Flask, render_template, redirect, flash, abort
from flask_bootstrap import Bootstrap
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy

# ------ SET APP
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

# --- SET DB
db = SQLAlchemy(app)
# --- LOGIN MANAGER
login_manager = LoginManager()
login_manager.init_app(app)


# ------ CONFIGURE TABLES
# --- CAFES DB
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


# --- USERS DB
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


# db.create_all()


# custom decorator that only allows admin to access certain views
def admin_only(func):
    @wraps(func)
    def wrapped_view(*args, **kwargs):
        user_id = int(current_user.get_id())
        if user_id != 1:
            return abort(403)
        return func(*args, **kwargs)

    return wrapped_view


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterUser()
    print(form.data)

    if form.validate_on_submit():
        # create new user record with hashed password
        new_user = User()
        new_user.email = form.email.data
        new_user.name = form.name.data
        new_user.password = generate_password_hash(password=form.password.data, method="pbkdf2:sha256", salt_length=8)
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect("/")
        except exc.IntegrityError:
            flash("Given email is already registered! Please log in.")
            return redirect("/login")
    else:
        return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginUser()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(pwhash=user.password, password=form.password.data):
            login_user(user)
            return redirect("/")
        else:
            flash("Email or password incorrect!")
    return render_template("login.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(user_id)
    if user:
        return user
    else:
        return None


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@login_required
@app.route("/add_cafe")
def add_cafe():
    form = AddCafe()
    return render_template("add_cafe.html", form=form)


@app.route("/about")
def about():
    pass
    return render_template("about.html")


@app.route("/cafes", methods=["POST", "GET"])
def cafes():
    form = FiltersForm()
    if form.validate_on_submit():
        if len(form.choices.data) == 4:
            selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_wifi=True, has_toilet=True,
                                                              can_take_calls=True)
        elif len(form.choices.data) == 3:
            if ["wifi", "toilet", "calls"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_wifi=True, has_toilet=True, can_take_calls=True)
            elif ["sockets", "toilet", "calls"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_toilet=True,
                                                                  can_take_calls=True)
            elif ["sockets", "wifi", "calls"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_wifi=True, can_take_calls=True)
            else:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_wifi=True, has_toilet=True)
        elif len(form.choices.data) == 2:
            if ["sockets", "wifi"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_wifi=True)
            elif ["sockets", "toilet"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, has_toilet=True)
            elif ["sockets", "calls"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True, can_take_calls=True)
            elif ["wifi", "toilet"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_wifi=True, has_toilet=True)
            elif ["wifi", "calls"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_wifi=True, can_take_calls=True)
            else:
                selected_cafes = db.session.query(Cafe).filter_by(has_toilet=True, can_take_calls=True)
        elif len(form.choices.data) == 1:
            if ["sockets"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_sockets=True)
            elif ["wifi"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_wifi=True)
            elif ["toilet"] == form.choices.data:
                selected_cafes = db.session.query(Cafe).filter_by(has_toilet=True)
            else:
                selected_cafes = db.session.query(Cafe).filter_by(can_take_calls=True)
        else:
            selected_cafes = db.session.query(Cafe).all()

        return render_template("cafes.html", cafes=selected_cafes, data=form.choices.data, form=form)
    else:
        all_cafes = db.session.query(Cafe).all()
        return render_template("cafes.html", cafes=all_cafes, form=form)


if __name__ == '__main__':
    app.run(debug=True)