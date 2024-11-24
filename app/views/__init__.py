# app/views/__init__.py

from flask import Blueprint, render_template

# Create a blueprint for main views
main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

# You can add more routes here as needed