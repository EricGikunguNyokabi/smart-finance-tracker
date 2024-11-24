# app/forms/auth.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           validators=[
                               DataRequired(),
                               Length(min=3, max=100, message="Username must be between 3 and 100 characters long")
                           ],
                           )
    email = StringField("Email",
                        validators=[
                            DataRequired(),
                            Email(message="Invalid email format"),
                            Length(max=255),
                        ],
                        )
    dob = DateField("Date of Birth", format='%Y-%m-%d', validators=[DataRequired()])  # Updated to DateField
    
    password = PasswordField("Password",
                             validators=[
                                 DataRequired(),
                                 Length(min=8, message="Password must be at least 8 characters long")
                             ],
                             )
    confirm_password = PasswordField("Confirm Password",  # Changed to consistent naming
                                     validators=[
                                         DataRequired(),
                                         EqualTo("password", message="Passwords do not match.")
                                     ],
                                     )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email",
                        validators=[
                            DataRequired(),
                            Email(message="Invalid email format")
                        ],)
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RequestOtp(FlaskForm):
    email = StringField("Email",
                        validators=[
                            DataRequired(),
                            Email(message="Invalid email format")
                        ],)
    submit = SubmitField("Request OTP")  # Changed to consistent naming


class VerifyOtp(FlaskForm):
    otp = StringField("OTP",
                      validators=[
                          DataRequired()
                      ])
    submit = SubmitField("Verify OTP")  # Changed to consistent naming


class ResetPassword(FlaskForm):
    password = PasswordField("Password",
                             validators=[
                                 DataRequired(),
                                 Length(min=8, message="Password must be at least 8 characters long")  # Added length validation
                             ]
                             )
    confirm_password = PasswordField("Confirm Password",  # Changed to consistent naming
                                     validators=[
                                         DataRequired(),
                                         EqualTo("password", message="Passwords do not match")
                                     ],
                                     )
    submit = SubmitField("Reset Password")  # Changed to consistent naming