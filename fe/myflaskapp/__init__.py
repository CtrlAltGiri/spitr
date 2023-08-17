from flask import Flask, g
from myflaskapp.blueprints.homepage.routes import homepage
from myflaskapp.blueprints.users.routes import users
from sqlalchemy import create_engine
from sqlalchemy.engine import URL 

app = Flask(__name__)
app.config.from_envvar('FE_SETTINGS')

@app.before_request
def before_request():
    if not g.engine:
        url = URL.create(
            drivername="postgresql",
            username= app.config["POSTGRES_USERNAME"],
            password= app.config["POSTGRES_PASSWORD"],
            host= app.config["POSTGRES_HOST"],
            port= app.config["POSTGRES_PORT"],
            database= app.config["POSTGRES_DATABASE"]
        )
        g.engine = create_engine(url)

app.register_blueprint(homepage)
app.register_blueprint(users)