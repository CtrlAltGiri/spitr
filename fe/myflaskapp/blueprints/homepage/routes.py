from flask import Blueprint, render_template

homepage = Blueprint('homepage', __name__, template_folder='templates')

@homepage.route("/", methods=["GET"])
def getHomePage():
        # if logged in, gg -> give it to em
        return render_template('homepage.html')