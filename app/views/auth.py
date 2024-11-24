# app/views/auth.py
from flask import Blueprint, request, render_template, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db
from app.forms.auth import RegistrationForm, LoginForm, RequestOtp, VerifyOtp, ResetPassword
from flask_login import login_user, logout_user, current_user


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            dob = form.dob.data
            password = form.password.data
            
            # Check if the email or username is already registered
            if User.query.filter_by(email=email).first():
                flash("Email already exists", "error")
                return render_template("auth/register.html", form=form)
            if User.query.filter_by(username=username).first():
                flash("Username already exists", "error")
                return render_template("auth/register.html", form=form)

            hashed_password = generate_password_hash(password)
            new_user = User(username=username, email=email, dob=dob, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("User  registered successfully", "success")
            return redirect(url_for('auth.login'))
        else:
            flash("There were errors in your form. Please correct them.", "error")

    return render_template("auth/register.html", form=form)



@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password, password):
                # Use Flask-Login's login_user method
                login_user(user)  # This will handle session management for you
                flash("Login successful", "success")

                # Redirect to the next page if it exists, otherwise redirect to main index
                next_page = request.args.get('next')
                return redirect(next_page or url_for("main.index"))

            flash("Invalid email or password", "error")

    return render_template("auth/login.html", form=form)
# from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
# import base64

# def custom_scrypt_check(stored_hash, password):
#     try:
#         # Parse the stored hash
#         parts = stored_hash.split("$")
#         if len(parts) != 3:
#             raise ValueError("Malformed scrypt hash.")
#         salt = base64.b64decode(parts[1])
#         stored_key = base64.b64decode(parts[2])

#         # Derive the key using the same scrypt parameters
#         kdf = Scrypt(
#             salt=salt,
#             length=len(stored_key),
#             n=32768,
#             r=8,
#             p=1,
#         )
#         derived_key = kdf.derive(password.encode())
#         return derived_key == stored_key
#     except Exception as e:
#         # Handle errors during scrypt validation
#         return False



# from werkzeug.security import generate_password_hash

# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if request.method == "POST":
#         if form.validate_on_submit():
#             email = form.email.data
#             password = form.password.data

#             # Query user by email
#             user = User.query.filter_by(email=email).first()
#             valid = False

#             if user:
#                 if user.password.startswith("scrypt:"):
#                     # Handle scrypt password verification
#                     valid = custom_scrypt_check(user.password, password)
#                 else:
#                     # Default Werkzeug check
#                     valid = check_password_hash(user.password, password)

#             if valid:
#                 # Rehash the password if it's a legacy `scrypt` hash
#                 if user.password.startswith("scrypt:"):
#                     user.password = generate_password_hash(password, method="pbkdf2:sha256")
#                     db.session.commit()  # Save the rehashed password

#                 # Successful login
#                 login_user(user)
#                 flash("Login successful", "success")

#                 # Redirect to the next page or index
#                 next_page = request.args.get('next')
#                 return redirect(next_page or url_for("main.index"))
#             else:
#                 flash("Invalid email or password", "error")

#     return render_template("auth/login.html", form=form)




@auth_bp.route("/request-otp", methods=["GET", "POST"])
def request_otp():
    form = RequestOtp()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.email.data
            user = User.query.filter_by(email=email).first()
            if user:
                # Implement OTP generation and sending logic here
                flash("OTP sent to your email", "success")
                return redirect(url_for('auth.verify_otp'))  # Redirect to verify OTP page
            else:
                flash("Email not found", "error")

    return render_template("auth/request_otp.html", form=form)

@auth_bp.route("/verify-otp", methods=["GET", "POST"])
def verify_otp():
    form = VerifyOtp()
    if request.method == "POST":
        if form.validate_on_submit():
            otp = form.otp.data
            email = form.email.data  # Assuming you are sending the email along with the OTP for verification

            user = User.query.filter_by(email=email).first()
            if user:
                # Implement OTP verification logic here
                flash("OTP verified successfully", "success")
                session['email'] = email  # Store email in session for password reset
                return redirect(url_for('auth.reset_password'))  # Redirect to reset password page
            else:
                flash("Email not found", "error")

    return render_template("auth/verify_otp.html", form=form)

@auth_bp.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    form = ResetPassword()
    if request.method == "POST":
        if form.validate_on_submit():
            password = form.password.data
            hashed_password = generate_password_hash(password)
            user = User.query.filter_by(email=session.get('email')).first()  # Get user from session
            if user:
                user.password = hashed_password
                db.session.commit()
                flash("Password reset successfully", "success")
                return redirect(url_for('auth.login'))  # Redirect to login after reset
            else:
                flash("User  not found", "error")

    return render_template("auth/reset_password.html", form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()  # Log the user out
    flash('You have been logged out.', 'success')  # Optional: flash a message
    return redirect(url_for("main.index"))