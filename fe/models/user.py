from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

class User(declarative_base()):
    __tablename__ = 'users'
    username = Column(String(50), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    display_name = Column(String(50), nullable=False)
    phone_number = Column(String(20))