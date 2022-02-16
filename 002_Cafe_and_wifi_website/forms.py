from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectMultipleField, widgets, IntegerField, BooleanField, \
    URLField
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.TableWidget(with_table_tag=True)
    option_widget = widgets.CheckboxInput()


class FiltersForm(FlaskForm):
    choices_list = [("sockets", "sockets"), ("wifi", "wifi"), ("toilet", "toilet"), ("calls", "calls")]
    choices = MultiCheckboxField(choices=choices_list)


# CREATE COMMENT FORM
class CreateCommentForm(FlaskForm):
    submit = SubmitField("Submit Comment")


# USERS REGISTER FORM
class RegisterUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


# USER LOGIN FORM
class LoginUser(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class AddCafe(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    map_url = URLField("Map URL", validators=[DataRequired()])
    img_url = URLField("Image URL", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    has_sockets = BooleanField("Has sockets", validators=[DataRequired()])
    has_wifi = BooleanField("Has WiFi", validators=[DataRequired()])
    has_toilet = BooleanField("Has toilet", validators=[DataRequired()])
    can_take_calls = BooleanField("Can take calls", validators=[DataRequired()])
    coffee_price = IntegerField("Coffee price", validators=[DataRequired()])
