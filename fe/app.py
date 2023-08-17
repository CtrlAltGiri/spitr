from flask import Flask, render_template, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine import URL 
from sqlalchemy.orm import sessionmaker
from models.user import User

app = Flask(__name__)
app.config.from_envvar('FE_SETTINGS')

# Create python connection to postgres server
url = URL.create(
    drivername="postgresql",
    username= app.config["POSTGRES_USERNAME"],
    password= app.config["POSTGRES_PASSWORD"],
    host= app.config["POSTGRES_HOST"],
    port= app.config["POSTGRES_PORT"],
    database= app.config["POSTGRES_DATABASE"]
)
engine = create_engine(url)

@app.route("/", methods=["GET"])
def getHomePage():
        # if logged in, gg -> give it to em
        
        # throw the homepsage otherwise
        return render_template('homepage.html')

@app.route("/register", methods=["GET"])
def getRegisterPage():
      return render_template('register.html')

@app.route("/register", methods=["POST"])
def createUser():
      # create new user, sends signal via rabbitMQ to email service
      return redirect('/login')

@app.route("/login", methods=["GET"])
def getLoginPage():
      Session = sessionmaker(bind=engine)
      session = Session()
      new_user = User(username='alice12345678', email='alice12345678@example.com', display_name='Alice', phone_number='1234567890')
      session.add(new_user)
      session.commit()
      return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
      return redirect('/test')

if __name__ == "__main__":
      app.run(debug=True)