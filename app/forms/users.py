# app/forms/users.py
from flask_wtf import FlaskForm
from wtforms import StringField,DateTimeField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo,Length