from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class Cred(declarative_base()):
    __tablename__ = 'credentials'
    username = Column(String(50), primary_key=True)
    password = Column(String(256), nullable=False)
    salt = Column(String(50), nullable=False)
    # createTime = Column(String(256))
    # lastModifiedTime = Column(String(256))
    # lastLoginTIme = Column(String(256))

class User(declarative_base()):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    displayname = Column(String(50), nullable=False)
    phone = Column(String(20))