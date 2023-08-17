import bcrypt
from myflaskapp.blueprints.users.models import User, Cred
from flask import Blueprint, render_template, redirect, request, g
from sqlalchemy.orm import sessionmaker

users = Blueprint('users', __name__)

@users.route("/register", methods=["GET"])
def getRegisterPage():
      return render_template('register.html')

@users.route("/register", methods=["POST"])
def createUser():
      userName, email, password, phonenumber, displayname = request.form.get("username"), request.form.get('email'), request.form.get('password').encode(), request.form.get('phonenumber'), request.form.get('displayname')
      salt = bcrypt.gensalt()
      hashed_password = bcrypt.hashpw(password, salt)

      Session = sessionmaker(bind=g.engine)
      session = Session()
      new_user = User(username=userName, email=email, displayname=displayname, phone=phonenumber)
      new_credential = Cred(username=userName, password=hashed_password.decode(), salt=salt.decode())
      session.add(new_user)
      session.add(new_credential)
      session.commit()
      # create new user, sends signal via rabbitMQ to email service
      return redirect('/login')

@users.route("/login", methods=["GET"])
def getLoginPage():
      return render_template('login.html')

@users.route("/login", methods=["POST"])
def login():
      userName = request.form.get("username")
      password = request.form.get('password').encode()

      Session = sessionmaker(bind=g.engine)
      session = Session()
      user_credential = session.query(Cred).filter_by(username=userName).first()
      if user_credential:
            stored_password = user_credential.password.encode()
            stored_salt = user_credential.salt.encode()
            hashed_password = bcrypt.hashpw(password, stored_salt)

            if hashed_password == stored_password:
                  return render_template('spitr.html')
      
      return redirect('/login')